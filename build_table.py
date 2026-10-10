"""Construit le tableau des bâtiments achevés en Suisse (2000-2024).

Sources (OFS) :
  * RegBL / GWR  (https://public.madd.bfs.admin.ch/ch.zip) : bâtiments, année de
    construction (GBAUJ), classe (GKLAS), emprise (GAREA), nombre d'étages (GASTW),
    volume (GVOL) et surface de référence énergétique (GEBF = SRE).
  * PX Web OFS : « Nouveaux bâtiments avec logements » (px-x-0904030000_102
    pour 2000-2012 et px-x-0904030000_106 pour 2013-2024), utilisé comme série
    officielle de contrôle pour les bâtiments d'habitation.

Usage :
    python build_table.py              # télécharge si nécessaire puis construit
    python build_table.py --no-download
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ZIP_PATH = DATA / "ch.zip"
REGBL_URL = "https://public.madd.bfs.admin.ch/ch.zip"
BUILDINGS_CSV = "gebaeude_batiment_edificio.csv"
OUTPUT = ROOT / "construction_suisse_2000_2024.csv"
YEARS = list(range(2000, 2025))

PX = "https://www.pxweb.bfs.admin.ch/api/v1/fr/"

CANTONS = ["ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL",
           "SH", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

# Regroupement des classes de bâtiment RegBL (GKLAS) -> type du tableau.
TYPES = {
    "Logement": ("Habitation : maisons à 1 ou 2 logements, immeubles, habitat communautaire (GKLAS 1110, 1121, 1122, 1130)",
                 {1110, 1121, 1122, 1130}),
    "Bureaux / commerce": ("Immeubles de bureaux et bâtiments commerciaux (GKLAS 1220, 1230)",
                           {1220, 1230}),
    "Enseignement": ("Bâtiments pour l'enseignement et la recherche (GKLAS 1263)", {1263}),
}
KLAS_TO_TYPE = {k: t for t, (_, ks) in TYPES.items() for k in ks}

# Statuts « bâtiment réalisé » : existant, non utilisable, démoli (achevé puis démoli).
COMPLETED_STATUS = {1004, 1005, 1007}


# --------------------------------------------------------------------------- RegBL
def download_regbl() -> None:
    DATA.mkdir(exist_ok=True)
    head = requests.head(REGBL_URL, allow_redirects=True, timeout=60)
    total = int(head.headers["content-length"])
    done = ZIP_PATH.stat().st_size if ZIP_PATH.exists() else 0
    if done == total:
        print(f"RegBL déjà téléchargé ({total / 1e6:.0f} Mo)")
        return
    if done > total:
        ZIP_PATH.unlink()
        done = 0
    print(f"Téléchargement du RegBL ({total / 1e6:.0f} Mo), reprise à {done / 1e6:.0f} Mo")
    headers = {"Range": f"bytes={done}-"} if done else {}
    with requests.get(REGBL_URL, headers=headers, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(ZIP_PATH, "ab" if done else "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)


def aggregate_regbl() -> pd.DataFrame:
    cols = ["GDEKT", "GSTAT", "GKLAS", "GBAUJ", "GAREA", "GVOL", "GASTW", "GEBF"]
    parts = []
    skipped_no_year = 0
    with zipfile.ZipFile(ZIP_PATH) as z, z.open(BUILDINGS_CSV) as fh:
        reader = pd.read_csv(fh, sep="\t", usecols=cols, dtype=str, chunksize=500_000,
                             encoding="utf-8")
        for i, ch in enumerate(reader, 1):
            for c in ("GSTAT", "GKLAS", "GBAUJ", "GAREA", "GVOL", "GASTW", "GEBF"):
                ch[c] = pd.to_numeric(ch[c], errors="coerce")
            ch = ch[ch["GSTAT"].isin(COMPLETED_STATUS) & ch["GKLAS"].isin(KLAS_TO_TYPE)]
            skipped_no_year += int(ch["GBAUJ"].isna().sum())
            ch = ch[ch["GBAUJ"].between(YEARS[0], YEARS[-1]) & ch["GDEKT"].isin(CANTONS)].copy()
            ch["Type de bâtiment"] = ch["GKLAS"].map(KLAS_TO_TYPE)
            ch["plancher"] = ch["GAREA"] * ch["GASTW"].clip(lower=1)
            ch["a_sre"] = ch["GEBF"].notna() & (ch["GEBF"] > 0)
            g = ch.groupby(["GBAUJ", "GDEKT", "Type de bâtiment"]).agg(
                n=("GKLAS", "size"),
                sre=("GEBF", "sum"),
                n_sre=("a_sre", "sum"),
                emprise=("GAREA", "sum"),
                plancher=("plancher", "sum"),
                volume=("GVOL", "sum"),
            )
            parts.append(g)
            print(f"  lot {i} traité", end="\r")
    print()
    print(f"Bâtiments des classes retenues sans année de construction (ignorés) : {skipped_no_year}")
    df = pd.concat(parts).groupby(level=[0, 1, 2]).sum().reset_index()
    df["GBAUJ"] = df["GBAUJ"].astype(int)
    return df


# --------------------------------------------------------------------------- PX Web
def px_new_residential() -> pd.DataFrame:
    """Nouveaux bâtiments avec logements par canton et année (OFS)."""
    out = []
    for table, ycode in (("px-x-0904030000_102", None), ("px-x-0904030000_106", None)):
        url = f"{PX}{table}/{table}.px"
        meta = requests.get(url, timeout=60).json()
        var_geo, var_type, var_year = meta["variables"]
        year_label = dict(zip(var_year["values"], var_year["valueTexts"]))
        query = {"query": [
            {"code": var_geo["code"], "selection": {"filter": "item", "values": CANTONS}},
            {"code": var_type["code"], "selection": {"filter": "item", "values": ["0"]}},
            {"code": var_year["code"], "selection": {"filter": "all", "values": ["*"]}},
        ], "response": {"format": "json"}}
        r = requests.post(url, json=query, timeout=120)
        r.raise_for_status()
        for row in r.json()["data"]:
            canton, _, y = row["key"]
            v = row["values"][0]
            out.append((int(year_label[y]), canton, int(v) if v not in ("", ".", "..", "...", "-") else None))
    df = pd.DataFrame(out, columns=["Année", "Canton", "n_ofs"])
    return df[df["Année"].between(YEARS[0], YEARS[-1])]


# --------------------------------------------------------------------------- Assemblage
def build() -> pd.DataFrame:
    reg = aggregate_regbl().rename(columns={"GBAUJ": "Année", "GDEKT": "Canton"})
    ofs = px_new_residential()

    grid = pd.MultiIndex.from_product([YEARS, CANTONS, list(TYPES)],
                                      names=["Année", "Canton", "Type de bâtiment"]).to_frame(index=False)
    df = grid.merge(reg, how="left", on=["Année", "Canton", "Type de bâtiment"])
    for c in ("n", "sre", "n_sre", "emprise", "plancher", "volume"):
        df[c] = df[c].fillna(0)
    df = df.merge(ofs, how="left", on=["Année", "Canton"])
    df.loc[df["Type de bâtiment"] != "Logement", "n_ofs"] = pd.NA

    out = pd.DataFrame({
        "Année": df["Année"],
        "Canton": df["Canton"],
        "Type de bâtiment": df["Type de bâtiment"],
        "Catégorie OFS": df["Type de bâtiment"].map(lambda t: TYPES[t][0]),
        "Nombre de bâtiments achevés (RegBL)": df["n"].astype(int),
        "Nouveaux bâtiments d'habitation (StatBL, contrôle)": df["n_ofs"].astype("Int64"),
        "Surface SRE (m²)": df["sre"].round(0).astype(int),
        "Bâtiments avec SRE renseignée": df["n_sre"].astype(int),
        "Emprise au sol (m²)": df["emprise"].round(0).astype(int),
        "Surface de plancher estimée (m²)": df["plancher"].round(0).astype(int),
        "Volume (m³)": df["volume"].round(0).astype(int),
        "Source / table OFS": df["Type de bâtiment"].map(
            lambda t: "RegBL (GWR) ; StatBL px-x-0904030000_102/_106" if t == "Logement" else "RegBL (GWR)"),
    })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-download", action="store_true")
    args = ap.parse_args()
    if not args.no_download:
        download_regbl()
    if not ZIP_PATH.exists():
        print("Fichier RegBL absent : lancez sans --no-download", file=sys.stderr)
        return 1
    df = build()
    df.to_csv(OUTPUT, index=False, encoding="utf-8-sig")
    print(f"{len(df)} lignes écrites dans {OUTPUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
