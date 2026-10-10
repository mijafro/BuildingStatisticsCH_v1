Il n’existe pas une seule série officielle qui donne, pour chaque année depuis 2000, la **SRE** et le **nombre de bâtiments construits** à la fois par type (logement, bureau, école) et par canton. Les données existent, mais elles sont réparties entre plusieurs statistiques de l’OFS et doivent être extraites de ses bases PX Web. [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master)

## Sources officielles

| Question | Source OFS | Ce qu’elle fournit |
|---|---|---|
| Bâtiments par canton, catégorie et période de construction | Statistique des bâtiments et des logements (StatBL), base PX Web | Nombre de bâtiments par canton, catégorie de bâtiment, année et période de construction.  [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/) |
| Logements achevés, autorisés et en construction | Statistique trimestrielle de la construction de logements | Séries annuelles de logements, surtout résidentiels.  [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master) |
| Constructions projetées et réalisées | Statistique suisse de la construction et des logements | Volumes, investissements et données par type d’ouvrage.  [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master) |
| Surface des bâtiments | StatBL / RegBL | Surfaces de référence énergétique ou surfaces utiles selon les tableaux, par canton et catégorie.  [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master) |

## Ce que les données montrent déjà

Pour les **bâtiments d’habitation**, la Suisse comptait environ 16 962 nouveaux bâtiments en 2000, 14 736 en 2010 et 12 190 en 2018 ; les nouvelles maisons individuelles sont passées de 13 768 en 2000 à 6 403 en 2018. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21000222100-12/package)

Le rythme de construction de logements reste d’environ **1% du parc existant par an**, selon l’Office fédéral du logement. [bwo.admin](https://www.bwo.admin.ch/fr/faits-et-chiffres-logement)

Pour l’ensemble du parc, 15% des bâtiments d’habitation avaient été construits après 2000 en 2017 ; cette part variait fortement selon les cantons, de 4% à Bâle-Ville à 24% à Fribourg. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue19099091700-05/package)

## Limites importantes

- **« Bâtiments construits par an »** : les séries les plus complètes portent souvent sur les **logements achevés** ou les **permis de construire**, et non sur tous les types de bâtiments achevés. [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master)
- **Bureaux et écoles** : ils sont classés dans les catégories de bâtiments non résidentiels ; les séries annuelles par canton existent dans StatBL, mais ne sont pas publiées sous forme d’un tableau unique « logement / bureau / école ». [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/)
- **SRE** : la surface de référence énergétique est surtout utilisée dans les labels et certaines statistiques énergétiques ; les statistiques de construction utilisent plus souvent la surface de plancher, la surface utile ou le volume. Il faut donc vérifier l’indicateur exact avant de comparer. [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master)
- **Cantons** : les données par canton sont disponibles, mais la désagrégation complète — année × canton × type × surface × bâtiments achevés — nécessite une extraction PX Web ou un téléchargement CSV. [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/)

## Comment obtenir le jeu de données complet

1. Ouvrir le catalogue PX Web de l’OFS : « Statistique des bâtiments et des logements ». [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/)
2. Choisir la table « Gebäudestruktur » : bâtiments selon canton, catégorie de bâtiment, nombre d’étages, période de construction et année. [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/)
3. Sélectionner les années 2000 à 2024, les 26 cantons et les catégories pertinentes : bâtiments d’habitation, bureaux/commerces, enseignement.
4. Exporter en CSV ou Excel, puis calculer les nouveaux bâtiments par différence entre les stocks annuels ou en utilisant les variables de période de construction.
5. Pour la SRE, croiser avec les données du RegBL ou les statistiques énergétiques cantonales, car la SRE n’est pas systématiquement publiée dans les mêmes tableaux que le nombre de bâtiments. [bfs.admin](https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master)

## Repères chiffrés

- **2000** : 16 962 nouveaux bâtiments d’habitation et 32 214 nouveaux logements. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21000222100-12/package)
- **2010** : 14 736 nouveaux bâtiments d’habitation et 43 632 nouveaux logements. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21000222100-12/package)
- **2018** : 12 190 nouveaux bâtiments d’habitation et 53 199 nouveaux logements. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21000222100-12/package)
- **Fin 2019** : environ 1,8 million de bâtiments d’habitation et 4,6 millions de logements en Suisse. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21099091900-05/package)
- **Après 2000** : surface moyenne des logements de 118 m², contre 109 m² pour ceux construits entre 1981 et 2000. [swissstats.bfs.admin](https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21099091900-05/package)

Si vous le souhaitez, je peux préparer un **tableau type** — années 2000–2024, 26 cantons, catégories logement/bureau/école, nombre de bâtiments et surface — que vous pourrez remplir à partir des exports OFS, ou je peux vous indiquer précisément les identifiants des tables PX Web à télécharger.


Voici le modèle de tableau à remplir, avec les tables OFS à utiliser. Le point clé : pour les **bâtiments achevés par année**, la source la plus fiable est le **RegBL/StatBL** ; pour les **nouveaux bâtiments d’habitation**, l’OFS publie aussi des séries spécifiques. [dam-api.bfs.admin](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36178239/master)

## Tableau à remplir

Créez un fichier CSV ou Excel avec cette structure. Une ligne = une combinaison année × canton × type de bâtiment.

| Année | Canton | Type de bâtiment | Nombre de bâtiments achevés | Surface SRE (m²) | Surface utile (m²) | Volume (m³) | Source / table OFS |
|---|---|---|---:|---:|---:|---:|---|
| 2000 | ZH | Logement |  |  |  |  | StatBL / RegBL |
| 2000 | ZH | Bureaux / commerce |  |  |  |  | StatBL / RegBL |
| 2000 | ZH | Enseignement |  |  |  |  | StatBL / RegBL |
| 2000 | GE | Logement |  |  |  |  | StatBL / RegBL |
| … | … | … |  |  |  |  |  |

Conseil : conservez séparément « bâtiments achevés », « permis accordés » et « logements achevés ». Ce sont trois indicateurs différents et ils ne doivent pas être additionnés. [bk.admin](https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/gebaudewohnungsstammdaten.pdf.download.pdf/Donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence%20des%20b%C3%A2timents%20et%20des%20logements.pdf)

## Tables OFS recommandées

| Besoin | Table PX Web OFS | Variables à sélectionner |
|---|---|---|
| Stock de bâtiments par canton, catégorie, période de construction et année | `px-x-0902020100_121` — « Gebäudestruktur » | Canton, catégorie de bâtiment, période de construction, année.  |
| Bâtiments par canton, type, propriétaire, époque et étages | `px-x-0902020100_106` | Canton, type de bâtiment, époque de construction, année.  [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/en/px-x-0902020100_106/px-x-0902020100_106/px-x-0902020100_106.px/) |
| Nouveaux bâtiments avec logements | `px-x-0904030000_102` | Canton, type de bâtiment, année ; couvre notamment 1995–2012 dans la version consultée.  [pxweb.bfs.admin](https://www.pxweb.bfs.admin.ch/pxweb/en/px-x-0904030000_102/px-x-0904030000_102/px-x-0904030000_102.px/) |
| Données détaillées par bâtiment : catégorie, statut, date de construction, surfaces, volume | RegBL — registre des bâtiments et des logements | `GBAUJ` année de construction, `GBAUP` époque, catégorie, statut « achevé », surfaces et volume.  [bk.admin](https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/gebaudewohnungsstammdaten.pdf.download.pdf/Donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence%20des%20b%C3%A2timents%20et%20des%20logements.pdf) |

## Catégories à utiliser

L’OFS ne classe pas les bâtiments exactement selon « logement / bureau / école ». Utilisez plutôt ses catégories officielles, puis regroupez-les :

| Votre catégorie | Catégories OFS à regrouper |
|---|---|
| Logement | Bâtiments exclusivement à usage d’habitation ; bâtiments principalement à usage d’habitation.  [dam-api.bfs.admin](https://dam-api.bfs.admin.ch/hub/api/dam/assets/36178239/master) |
| Bureaux | Bâtiments à usage commercial ou de services, selon la nomenclature détaillée de la catégorie de bâtiment.  [bfs.admin](https://www.bfs.admin.ch/bfs/fr/home/statistiques/construction-logement/batiments/categorie.html) |
| Écoles | Bâtiments d’enseignement, catégorie spécifique de la nomenclature OFS.  [bfs.admin](https://www.bfs.admin.ch/bfs/fr/home/statistiques/construction-logement/batiments/categorie.html) |

## Méthode de calcul

1. Téléchargez les données RegBL ou StatBL pour les années 2000 à 2024.
2. Filtrez le statut du bâtiment sur **« achevé »** et l’année de construction sur l’année souhaitée.
3. Regroupez par canton et catégorie de bâtiment.
4. Additionnez le nombre de bâtiments, puis les surfaces et volumes.
5. Pour la SRE, utilisez uniquement les jeux qui la contiennent explicitement ; sinon, indiquez « surface utile » ou « surface de plancher » et ne la présentez pas comme de la SRE. [bk.admin](https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/gebaudewohnungsstammdaten.pdf.download.pdf/Donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence%20des%20b%C3%A2timents%20et%20des%20logements.pdf)

## Mise en garde sur la SRE

La **SRE** est un indicateur énergétique normalisé, utilisé notamment par Minergie et les statistiques énergétiques ; elle n’est pas toujours identique à la surface de plancher ou à la surface utile des statistiques de construction. 

Pour une analyse énergétique ou carbone, il vaut donc mieux :
- utiliser la SRE lorsqu’elle est disponible ;
- sinon, documenter clairement l’indicateur de surface utilisé ;
- éviter de convertir automatiquement surface utile en SRE, car les coefficients varient selon le type de bâtiment. 

## Export pratique

Je vous conseille de produire deux fichiers :

- `construction_suisse_2000_2024_batiments.csv` : année, canton, catégorie OFS, nombre de bâtiments achevés.
- `construction_suisse_2000_2024_surfaces.csv` : année, canton, catégorie OFS, surface disponible, type de surface, unité.

Vous pourrez ensuite créer un tableau croisé dynamique avec :
- **lignes** : année, canton ;
- **colonnes** : logement, bureaux, écoles ;
- **valeurs** : nombre de bâtiments et surface.