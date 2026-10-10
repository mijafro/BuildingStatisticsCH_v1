# BuildingStatisticsCH

Tableau et tableau de bord des **bâtiments achevés en Suisse entre 2000 et 2024**, par année, canton et type de bâtiment (logement, bureaux / commerce, enseignement), avec nombre de bâtiments, surface de référence énergétique (SRE), emprise au sol, surface de plancher estimée et volume.

Les données proviennent de l'Office fédéral de la statistique (OFS). Le projet les télécharge, les agrège dans un CSV, puis génère un tableau de bord HTML autonome.

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `plan.md` | Notes de départ : sources OFS identifiées, limites, structure cible du tableau |
| `build_table.py` | Télécharge le RegBL et les tables PX Web, agrège et écrit le CSV |
| `build_dashboard.py` | Génère `dashboard.html` à partir du CSV |
| `dashboard_template.html` | Gabarit HTML/JS du tableau de bord (données injectées à la génération) |
| `construction_suisse_2000_2024.csv` | Tableau final (1 950 lignes) |
| `dashboard.html` | Tableau de bord autonome (généré) |
| `data/ch.zip` | Copie locale du RegBL (948 Mo, téléchargée automatiquement, hors suivi conseillé) |
| `requirements.txt` | Dépendances Python (`pandas`, `requests`) |

## Utilisation

Prérequis : Python 3.10 ou plus, environ 1 Go d'espace disque et une connexion internet pour la première exécution.

```powershell
pip install -r requirements.txt

python build_table.py            # télécharge le RegBL si besoin, construit le CSV
python build_table.py --no-download   # réutilise data/ch.zip déjà présent

python build_dashboard.py        # génère dashboard.html
```

Puis ouvrir `dashboard.html` dans un navigateur (aucun serveur ni connexion nécessaire).

Remarques :
- Le téléchargement du RegBL (948 Mo) peut durer plusieurs minutes. Il reprend là où il s'est arrêté s'il est interrompu.
- L'agrégation du RegBL (fichier de 658 Mo) se fait par lots et prend quelques minutes.
- Le RegBL est mis à jour en continu par l'OFS : relancer le script plus tard peut donner des chiffres légèrement différents, surtout pour les années récentes. Supprimez `data/ch.zip` pour forcer un nouveau téléchargement.

## Structure du CSV

Une ligne par combinaison année × canton × type de bâtiment (25 × 26 × 3 = 1 950). Encodage UTF-8 avec BOM (lisible directement dans Excel), séparateur virgule.

| Colonne | Contenu |
|---|---|
| Année | Année de construction (2000–2024) |
| Canton | Sigle du canton (26 cantons) |
| Type de bâtiment | Logement, Bureaux / commerce, Enseignement |
| Catégorie OFS | Classes de bâtiment RegBL regroupées dans ce type |
| Nombre de bâtiments achevés (RegBL) | Nombre de bâtiments dont l'année de construction est l'année indiquée |
| Nouveaux bâtiments d'habitation (StatBL, contrôle) | Série officielle de l'OFS, renseignée uniquement pour le type Logement (vide sinon) |
| Surface SRE (m²) | Somme des SRE renseignées |
| Bâtiments avec SRE renseignée | Nombre de bâtiments contribuant à la colonne SRE |
| Emprise au sol (m²) | Somme de la surface bâtie au sol |
| Surface de plancher estimée (m²) | Emprise au sol × nombre d'étages (estimation) |
| Volume (m³) | Somme des volumes |
| Source / table OFS | Source utilisée pour la ligne |

Une valeur de 0 signifie « aucun bâtiment trouvé ou aucune surface renseignée », pas « donnée inconnue ». Pour distinguer les deux cas pour la SRE, utiliser la colonne « Bâtiments avec SRE renseignée ».

## Fonctionnalités du tableau de bord

**Filtres globaux** : plage d'années, type de bâtiment, grande région, canton (avec boutons « tous » et « aucun »). Ils s'appliquent à toute la page.

**Indicateurs** : total des bâtiments (RegBL), nouveaux bâtiments d'habitation (StatBL), SRE renseignée, volume, part de bâtiments avec SRE.

**Graphique et tableau croisé**
- Mesure, axe X et séries au choix parmi les dimensions : Année, Période de 5 ans, Canton, Grande région, Type de bâtiment.
- Agrégation : somme, moyenne, minimum, maximum.
- Types de graphique : lignes, barres groupées, barres empilées. Infobulles au survol.
- Nombre maximal de séries (les suivantes sont regroupées en « Autres » pour la somme) et tri de l'axe X par valeur.
- Tableau croisé correspondant, avec totaux (pour la somme) et export CSV.

**Tableau détaillé**
- Regroupement par une ou plusieurs dimensions, choix libre des colonnes, tri par clic sur l'en-tête, ligne de total, export CSV.

**Mesures disponibles** : les sept mesures du CSV, plus cinq mesures calculées :

| Mesure calculée | Formule |
|---|---|
| SRE moyenne par bâtiment renseigné | SRE / bâtiments avec SRE renseignée |
| Part de bâtiments avec SRE (%) | 100 × bâtiments avec SRE / bâtiments achevés |
| Plancher estimé moyen par bâtiment | Surface de plancher estimée / bâtiments achevés |
| Volume moyen par bâtiment | Volume / bâtiments achevés |
| Écart RegBL vs StatBL (%) | 100 × (RegBL − StatBL) / StatBL |

Les mesures calculées sont dérivées des sommes de chaque groupe. Les agrégations moyenne, minimum et maximum ne leur sont pas appliquées. Pour les autres mesures, la « moyenne » porte sur les lignes sources (année × canton × type), pas sur les bâtiments individuels. Les grandes régions (7) sont déduites du canton dans le tableau de bord, selon la nomenclature de l'OFS ; elles ne figurent pas dans le CSV.

## Sources de données

1. **RegBL / GWR** (Registre fédéral des bâtiments et des logements) : `https://public.madd.bfs.admin.ch/ch.zip`. On utilise le fichier `gebaeude_batiment_edificio.csv` avec les champs `GDEKT` (canton), `GSTAT` (statut), `GKLAS` (classe de bâtiment), `GBAUJ` (année de construction), `GAREA` (emprise), `GASTW` (nombre d'étages), `GVOL` (volume) et `GEBF` (surface de référence énergétique). Source principale du tableau.
2. **PX Web OFS**, « Nouveaux bâtiments avec logements » par canton et année : `px-x-0904030000_102` (2000–2012) et `px-x-0904030000_106` (2013–2024), mesure « total des bâtiments avec logements ». Source officielle de contrôle pour les bâtiments d'habitation.

Les tables de stock citées dans `plan.md` (`px-x-0902020100_121` et `_106`) ne couvrent que jusqu'au recensement de 2000 : elles n'ont pas été utilisées. Aucune table PX Web ne donne le nombre de bâtiments non résidentiels achevés par canton et année ; les séries de dépenses de construction (`px-x-0904010000_20x`) sont en francs, pas en bâtiments.

Les données de l'OFS sont soumises aux conditions d'utilisation de l'OFS (voir `license.pdf` dans l'archive RegBL). Citer l'OFS comme source en cas de réutilisation.

## Calculs et hypothèses

**Nombre de bâtiments achevés.** On compte les bâtiments du RegBL dont :
- la classe `GKLAS` appartient à l'un des regroupements ci-dessous ;
- le statut `GSTAT` est 1004 (existant), 1005 (non utilisable) ou 1007 (démoli) ;
- l'année de construction `GBAUJ` est comprise entre 2000 et 2024 ;
- le canton `GDEKT` est l'un des 26 cantons.

Les bâtiments démolis sont inclus (hypothèse : un bâtiment construit puis démoli a bien été achevé). Les bâtiments en projet, autorisés, en construction ou non réalisés (1001, 1002, 1003, 1008) sont exclus. L'année de construction est supposée être l'année d'achèvement.

**Surfaces et volume.** Somme des champs `GEBF` (SRE), `GAREA` (emprise) et `GVOL` (volume) sur les bâtiments retenus. Les valeurs absentes ne sont pas comptées (elles ne valent pas zéro, elles sont ignorées).

**Surface de plancher estimée.** `GAREA × max(GASTW, 1)` par bâtiment. C'est une approximation : elle suppose que tous les étages ont la même surface que l'emprise, et ignore les sous-sols, les combles et les niveaux partiels. Elle n'est pas une SRE et ne doit pas être présentée comme telle.

**SRE.** Reprise telle que renseignée dans le RegBL (`GEBF`). Aucune conversion à partir d'une autre surface, car les coefficients varient selon le type de bâtiment.

**Série de contrôle StatBL.** Nombre total de « nouveaux bâtiments avec logements » par canton et année, joint à la ligne Logement. Les deux tables PX Web sont mises bout à bout (changement de série en 2013).

## Regroupements considérés

Les catégories « logement / bureau / école » ne correspondent pas exactement à la nomenclature de l'OFS. Regroupement retenu, sur la classe de bâtiment `GKLAS` :

| Type du tableau | Classes RegBL (`GKLAS`) |
|---|---|
| Logement | 1110 maison à un logement, 1121 maison à deux logements, 1122 immeuble à trois logements ou plus, 1130 habitat communautaire |
| Bureaux / commerce | 1220 immeuble de bureaux, 1230 bâtiment commercial |
| Enseignement | 1263 bâtiment pour l'enseignement et la recherche |

Les autres classes ne figurent pas dans le tableau : hôtels et hébergement (1211, 1212), restauration (1231), transports et garages (1241, 1242), industrie et entrepôts (1251, 1252), culture, musées, santé, sport (1261, 1262, 1264, 1265), agriculture (1271, 1276 à 1278), cultes (1272) et autres. Les bâtiments mixtes sont classés selon leur seule classe `GKLAS` : un immeuble mixte classé en 1220 compte comme bureau, pas comme logement. La classe 1263 inclut la recherche, pas seulement les écoles. Le type « Bureaux / commerce » regroupe bureaux et commerces, qui ne sont pas séparés dans le tableau.

Grandes régions (tableau de bord) : Région lémanique (VD, VS, GE) ; Espace Mittelland (BE, FR, SO, NE, JU) ; Suisse du Nord-Ouest (BS, BL, AG) ; Zurich (ZH) ; Suisse orientale (GL, SH, AR, AI, SG, GR, TG) ; Suisse centrale (LU, UR, SZ, OW, NW, ZG) ; Tessin (TI).

## Réserves

1. **Couverture insuffisante du RegBL avant 2003.** Pour le logement, le RegBL donne 9 197 bâtiments en 2000 contre 16 962 selon l'OFS. Entre 2003 et 2024, l'écart reste de l'ordre de 2 à 8 %. Pour 2000–2002, utiliser la colonne StatBL (logement uniquement). Les chiffres RegBL de ces années pour les bureaux et l'enseignement sont vraisemblablement sous-estimés.
2. **SRE très partiellement renseignée.** Environ 9 % des bâtiments avant 2016, 32 % en 2020 et 88 % en 2024. Les sommes de SRE ne sont donc pas comparables entre années, ni entre cantons sans vérifier la part de bâtiments renseignés. Utiliser les mesures « Bâtiments avec SRE renseignée » et « SRE moyenne / bât. renseigné ». Ne pas multiplier une SRE moyenne par le nombre total de bâtiments sans en mesurer le biais (les bâtiments renseignés peuvent ne pas être représentatifs).
3. **Survie des bâtiments.** Seuls les bâtiments encore enregistrés sont comptés. Les démolitions anciennes non saisies dans le RegBL ne figurent pas, ce qui sous-estime légèrement les bâtiments achevés d'une année donnée.
4. **Année de construction manquante.** Les bâtiments sans `GBAUJ` sont ignorés (le script affiche leur nombre, tous millésimes confondus).
5. **Bureaux et enseignement : source unique.** Aucune série officielle indépendante ne permet de contrôler ces deux types.
6. **Qualité de saisie.** Le RegBL est alimenté par les communes. La classe de bâtiment, les étages, les surfaces et les volumes peuvent contenir des erreurs ou des valeurs aberrantes ; aucune correction n'a été appliquée.
7. **Surface de plancher et emprise** : voir les limites de l'estimation ci-dessus. Le volume (`GVOL`) peut selon les cas provenir de différentes normes (volume SIA 416 ou estimation).
8. **Indicateurs distincts.** Bâtiments achevés, logements achevés et permis de construire sont trois indicateurs différents. Ce projet ne traite que les bâtiments achevés (et, en contrôle, les nouveaux bâtiments avec logements) ; il ne faut pas les additionner à d'autres.
9. **Données récentes.** 2023 et 2024 sont susceptibles d'être révisés lors des prochaines mises à jour du RegBL (saisies tardives).
10. **Valeurs à 0.** Dans le CSV, 0 signifie « rien de trouvé » : ce n'est pas une preuve qu'aucun bâtiment n'a été construit (voir réserves 1 et 4).
