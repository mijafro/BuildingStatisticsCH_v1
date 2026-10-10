"""Génère dashboard.html (autonome, sans serveur) à partir du CSV produit par build_table.py.

    python build_dashboard.py
Puis ouvrir dashboard.html dans un navigateur.
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "construction_suisse_2000_2024.csv", encoding="utf-8-sig")
# ordre : année, canton, type, n, ofs, sre, nsre, emprise, plancher, volume
cols = df.columns[[0, 1, 2, 4, 5, 6, 7, 8, 9, 10]]
rows = [[None if pd.isna(v) else (v.item() if hasattr(v, "item") else v) for v in r]
        for r in df[cols].itertuples(index=False)]
html = (ROOT / "dashboard_template.html").read_text(encoding="utf-8")
html = html.replace("/*DATA*/", json.dumps(rows, ensure_ascii=False, separators=(",", ":")))
out = ROOT / "dashboard.html"
out.write_text(html, encoding="utf-8")
print(f"{out.name} écrit ({out.stat().st_size / 1024:.0f} Ko, {len(rows)} lignes)")
