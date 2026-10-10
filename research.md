# Quels sont les chiffres de la construction suisse depuis 2000 : surface SRE et nombre de bâtiments construis par an, par type de bâtiment (logement, bureau, école) et par canton

Il n’existe pas une seule série officielle qui donne, pour chaque année depuis 2000, la **SRE** et le **nombre de bâtiments construits** à la fois par type (logement, bureau, école) et par canton. Les données existent, mais elles sont réparties entre plusieurs statistiques de l’OFS et doivent être extraites de ses bases PX Web.[^2_1][^2_2]

## Sources officielles

| Question | Source OFS | Ce qu’elle fournit |
| :-- | :-- | :-- |
| Bâtiments par canton, catégorie et période de construction | Statistique des bâtiments et des logements (StatBL), base PX Web | Nombre de bâtiments par canton, catégorie de bâtiment, année et période de construction. [^2_2] |
| Logements achevés, autorisés et en construction | Statistique trimestrielle de la construction de logements | Séries annuelles de logements, surtout résidentiels. [^2_1] |
| Constructions projetées et réalisées | Statistique suisse de la construction et des logements | Volumes, investissements et données par type d’ouvrage. [^2_1] |
| Surface des bâtiments | StatBL / RegBL | Surfaces de référence énergétique ou surfaces utiles selon les tableaux, par canton et catégorie. [^2_1][^2_2] |

## Ce que les données montrent déjà

Pour les **bâtiments d’habitation**, la Suisse comptait environ 16 962 nouveaux bâtiments en 2000, 14 736 en 2010 et 12 190 en 2018 ; les nouvelles maisons individuelles sont passées de 13 768 en 2000 à 6 403 en 2018.[^2_3]

Le rythme de construction de logements reste d’environ **1% du parc existant par an**, selon l’Office fédéral du logement.[^2_4]

Pour l’ensemble du parc, 15% des bâtiments d’habitation avaient été construits après 2000 en 2017 ; cette part variait fortement selon les cantons, de 4% à Bâle-Ville à 24% à Fribourg.[^2_5]

## Limites importantes

- **« Bâtiments construits par an »** : les séries les plus complètes portent souvent sur les **logements achevés** ou les **permis de construire**, et non sur tous les types de bâtiments achevés.[^2_1]
- **Bureaux et écoles** : ils sont classés dans les catégories de bâtiments non résidentiels ; les séries annuelles par canton existent dans StatBL, mais ne sont pas publiées sous forme d’un tableau unique « logement / bureau / école ».[^2_2]
- **SRE** : la surface de référence énergétique est surtout utilisée dans les labels et certaines statistiques énergétiques ; les statistiques de construction utilisent plus souvent la surface de plancher, la surface utile ou le volume. Il faut donc vérifier l’indicateur exact avant de comparer.[^2_1]
- **Cantons** : les données par canton sont disponibles, mais la désagrégation complète — année × canton × type × surface × bâtiments achevés — nécessite une extraction PX Web ou un téléchargement CSV.[^2_2]


## Comment obtenir le jeu de données complet

1. Ouvrir le catalogue PX Web de l’OFS : « Statistique des bâtiments et des logements ».[^2_2]
2. Choisir la table « Gebäudestruktur » : bâtiments selon canton, catégorie de bâtiment, nombre d’étages, période de construction et année.[^2_2]
3. Sélectionner les années 2000 à 2024, les 26 cantons et les catégories pertinentes : bâtiments d’habitation, bureaux/commerces, enseignement.
4. Exporter en CSV ou Excel, puis calculer les nouveaux bâtiments par différence entre les stocks annuels ou en utilisant les variables de période de construction.
5. Pour la SRE, croiser avec les données du RegBL ou les statistiques énergétiques cantonales, car la SRE n’est pas systématiquement publiée dans les mêmes tableaux que le nombre de bâtiments.[^2_1]

## Repères chiffrés

- **2000** : 16 962 nouveaux bâtiments d’habitation et 32 214 nouveaux logements.[^2_3]
- **2010** : 14 736 nouveaux bâtiments d’habitation et 43 632 nouveaux logements.[^2_3]
- **2018** : 12 190 nouveaux bâtiments d’habitation et 53 199 nouveaux logements.[^2_3]
- **Fin 2019** : environ 1,8 million de bâtiments d’habitation et 4,6 millions de logements en Suisse.[^2_6]
- **Après 2000** : surface moyenne des logements de 118 m², contre 109 m² pour ceux construits entre 1981 et 2000.[^2_6]

Si vous le souhaitez, je peux préparer un **tableau type** — années 2000–2024, 26 cantons, catégories logement/bureau/école, nombre de bâtiments et surface — que vous pourrez remplir à partir des exports OFS, ou je peux vous indiquer précisément les identifiants des tables PX Web à télécharger.

<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master

[^2_2]: https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/

[^2_3]: https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21000222100-12/package

[^2_4]: https://www.bwo.admin.ch/fr/faits-et-chiffres-logement

[^2_5]: https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue19099091700-05/package

[^2_6]: https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue21099091900-05/package

[^2_7]: https://www.bfs.admin.ch/bfs/rm/home.gnpdetail.2024-0526.html

[^2_8]: https://dam-api.bfs.admin.ch/hub/api/dam/assets/32329525/master

[^2_9]: https://www.bfs.admin.ch/news/de/2022-0075

[^2_10]: https://www.swissstats.bfs.admin.ch/data/webviewer/appId/ch.admin.bfs.swissstat/article/issue19099081700-05/package

[^2_11]: https://www.bfs.admin.ch/news/de/2023-0442

[^2_12]: https://statistique.ge.ch/tel/publications/2021/informations_statistiques/construction_etat_mouvement/is_construmouv_05_2021.pdf

[^2_13]: https://www.bfs.admin.ch/bfsstatic/dam/assets/347231/master

[^2_14]: https://dam-api.bfs.admin.ch/hub/api/dam/assets/36141950/master

[^2_15]: https://dam-api.bfs.admin.ch/hub/api/dam/assets/32411360/master


---

# oui

Voici le modèle de tableau à remplir, avec les tables OFS à utiliser. Le point clé : pour les **bâtiments achevés par année**, la source la plus fiable est le **RegBL/StatBL** ; pour les **nouveaux bâtiments d’habitation**, l’OFS publie aussi des séries spécifiques.[^3_1][^3_2][^3_3]

## Tableau à remplir

Créez un fichier CSV ou Excel avec cette structure. Une ligne = une combinaison année × canton × type de bâtiment.


| Année | Canton | Type de bâtiment | Nombre de bâtiments achevés | Surface SRE (m²) | Surface utile (m²) | Volume (m³) | Source / table OFS |
| :-- | :-- | :-- | --: | --: | --: | --: | :-- |
| 2000 | ZH | Logement |  |  |  |  | StatBL / RegBL |
| 2000 | ZH | Bureaux / commerce |  |  |  |  | StatBL / RegBL |
| 2000 | ZH | Enseignement |  |  |  |  | StatBL / RegBL |
| 2000 | GE | Logement |  |  |  |  | StatBL / RegBL |
| … | … | … |  |  |  |  |  |

Conseil : conservez séparément « bâtiments achevés », « permis accordés » et « logements achevés ». Ce sont trois indicateurs différents et ils ne doivent pas être additionnés.[^3_2][^3_4]

## Tables OFS recommandées

| Besoin | Table PX Web OFS | Variables à sélectionner |
| :-- | :-- | :-- |
| Stock de bâtiments par canton, catégorie, période de construction et année | `px-x-0902020100_121` — « Gebäudestruktur » | Canton, catégorie de bâtiment, période de construction, année. [^3_5] |
| Bâtiments par canton, type, propriétaire, époque et étages | `px-x-0902020100_106` | Canton, type de bâtiment, époque de construction, année. [^3_6] |
| Nouveaux bâtiments avec logements | `px-x-0904030000_102` | Canton, type de bâtiment, année ; couvre notamment 1995–2012 dans la version consultée. [^3_3] |
| Données détaillées par bâtiment : catégorie, statut, date de construction, surfaces, volume | RegBL — registre des bâtiments et des logements | `GBAUJ` année de construction, `GBAUP` époque, catégorie, statut « achevé », surfaces et volume. [^3_2] |

## Catégories à utiliser

L’OFS ne classe pas les bâtiments exactement selon « logement / bureau / école ». Utilisez plutôt ses catégories officielles, puis regroupez-les :


| Votre catégorie | Catégories OFS à regrouper |
| :-- | :-- |
| Logement | Bâtiments exclusivement à usage d’habitation ; bâtiments principalement à usage d’habitation. [^3_1] |
| Bureaux | Bâtiments à usage commercial ou de services, selon la nomenclature détaillée de la catégorie de bâtiment. [^3_7] |
| Écoles | Bâtiments d’enseignement, catégorie spécifique de la nomenclature OFS. [^3_7] |

## Méthode de calcul

1. Téléchargez les données RegBL ou StatBL pour les années 2000 à 2024.
2. Filtrez le statut du bâtiment sur **« achevé »** et l’année de construction sur l’année souhaitée.
3. Regroupez par canton et catégorie de bâtiment.
4. Additionnez le nombre de bâtiments, puis les surfaces et volumes.
5. Pour la SRE, utilisez uniquement les jeux qui la contiennent explicitement ; sinon, indiquez « surface utile » ou « surface de plancher » et ne la présentez pas comme de la SRE.[^3_4][^3_2]

## Mise en garde sur la SRE

La **SRE** est un indicateur énergétique normalisé, utilisé notamment par Minergie et les statistiques énergétiques ; elle n’est pas toujours identique à la surface de plancher ou à la surface utile des statistiques de construction.[^3_4]

Pour une analyse énergétique ou carbone, il vaut donc mieux :

- utiliser la SRE lorsqu’elle est disponible ;
- sinon, documenter clairement l’indicateur de surface utilisé ;
- éviter de convertir automatiquement surface utile en SRE, car les coefficients varient selon le type de bâtiment.[^3_4]


## Export pratique

Je vous conseille de produire deux fichiers :

- `construction_suisse_2000_2024_batiments.csv` : année, canton, catégorie OFS, nombre de bâtiments achevés.
- `construction_suisse_2000_2024_surfaces.csv` : année, canton, catégorie OFS, surface disponible, type de surface, unité.

Vous pourrez ensuite créer un tableau croisé dynamique avec :

- **lignes** : année, canton ;
- **colonnes** : logement, bureaux, écoles ;
- **valeurs** : nombre de bâtiments et surface.

<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://dam-api.bfs.admin.ch/hub/api/dam/assets/36178239/master

[^3_2]: https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/gebaudewohnungsstammdaten.pdf.download.pdf/Données de référence des bâtiments et des logements.pdf

[^3_3]: https://www.pxweb.bfs.admin.ch/pxweb/en/px-x-0904030000_102/px-x-0904030000_102/px-x-0904030000_102.px/

[^3_4]: https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master

[^3_5]: https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-0902020100_121/-/px-x-0902020100_121.px/

[^3_6]: https://www.pxweb.bfs.admin.ch/pxweb/en/px-x-0902020100_106/px-x-0902020100_106/px-x-0902020100_106.px/

[^3_7]: https://www.bfs.admin.ch/bfs/fr/home/statistiques/construction-logement/batiments/categorie.html

[^3_8]: https://statistique.ge.ch/graphiques_js/09/09_02/G09_02_02.xls

[^3_9]: https://dam-api.bfs.admin.ch/hub/api/dam/assets/27905170/master

[^3_10]: https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0903020000_101/-/px-x-0903020000_101.px/

[^3_11]: https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0102030000_101/

[^3_12]: https://www.pxweb.bfs.admin.ch/pxweb/en/px-x-0902020100_152/px-x-0902020100_152/px-x-0902020100_152.px/

[^3_13]: https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0102010000_101/

[^3_14]: https://www.pxweb.bfs.admin.ch/pxweb/fr/

[^3_15]: https://www.pxweb.bfs.admin.ch/pxweb/en/px-x-0103010000_324/


---

# Je veux ajouter ou modifier des éléments du tableau. Pour chaque proposition indique moi si la donnée est disponible et si oui à quel endroit.

- Distinguer Habitation et Logement : le nombre de bâtiment d'habitation est différent du nombre de logements puisqu'un bâtiment d'habitation peut contenir plusieurs logements. Il faut distinguer dans type de bâtiment "habitation" et il faudrait compter le nombre de nouveaux logements par an.
- Est-ce possible de distinguer également les logements par nombre de pièces ? En faisant attention à la définition du nombre de pièce qui peut varier d'un canton à un autre et en proposant une explication pour interpréter correctement ce nb de pièce selon le canton (conversion, etc.).
- Pour un nouveau bâtiment achevé, est-ce possible de savoir si sa construction suit la déconstruction d'un autre bâtiment, s'il a été construit sur une zone déjà urbanisée (participe à la densification) ou si le bâtiment a été construit sur une zone qui n'était pas urbanisée (participer à l'urbanisation) ?
- Est-ce possible de compter le nombre de niveau pour chaque nouveau bâtiment construit ?
- Est-ce possible de compter le nombre de bâtiment déconstruit chaque année accompagné des mêmes caractéristiques que pour les nouvelles constructions : canton, surface sre et utile, volume, nombre de niveaux, nombre de logement (1 seul si c'est une maison individuelle par exemple) ?
- Est-ce possible de recenser les formes géométriques des bâtiments (forme 2D de l'emprise au sol, nombre de niveau et hauteur totale du bâtiment) ?

Oui — la plupart de vos ajouts sont possibles, mais à des niveaux de fiabilité très différents. Le **RegBL** est la source centrale pour les bâtiments et logements ; il contient notamment le statut, les dates de construction/démolition, les surfaces, le volume, le nombre d’étages et le nombre de pièces.[^4_1][^4_2][^4_3]

## Synthèse de disponibilité

| Élément souhaité | Disponible ? | Source principale | Fiabilité / limite |
| :-- | :-- | :-- | :-- |
| Bâtiments d’habitation vs nombre de logements | **Oui** | RegBL, StatBL, OFS | Très bonne : `EGID` pour le bâtiment, `EWID` pour le logement. [^4_4][^4_2] |
| Nouveaux logements par an | **Oui** | OFS, statistique des constructions et logements ; RegBL | Bonne, surtout pour les logements achevés. [^4_5][^4_2] |
| Logements par nombre de pièces | **Oui** | RegBL, PX Web OFS | Bonne, avec une définition fédérale homogène. [^4_6][^4_7][^4_3] |
| Nouvelle construction après démolition | **Partiellement** | RegBL + cadastre / données cantonales | Le lien explicite « démolition → nouvelle construction » n’est pas une variable standard du RegBL. [^4_1][^4_8] |
| Construction en zone déjà urbanisée / densification | **Partiellement** | RegBL + cadastre, zones d’affectation, MOcad, données cantonales | Possible par analyse géospatiale, mais pas comme attribut direct. [^4_9][^4_4] |
| Nombre de niveaux | **Oui** | RegBL | Nombre d’étages enregistré au niveau du bâtiment. [^4_1][^4_6][^4_2] |
| Bâtiments démolis par an | **Oui** | RegBL | Statut « démoli » et année de démolition `GABBJ`. [^4_1][^4_8][^4_2] |
| Caractéristiques des bâtiments démolis | **Partiellement** | RegBL | Canton, catégorie, surfaces, volume, étages, logements : oui ; SRE : généralement non. [^4_1][^4_2][^4_3] |
| Forme 2D de l’emprise au sol | **Oui** | Cadastre, swissBUILDINGS3D, géodonnées cantonales | Bonne, mais dépend de la source géomatique. [^4_9] |
| Hauteur totale du bâtiment | **Partiellement** | swissBUILDINGS3D, modèles 3D cantonaux | Pas un attribut standard du RegBL. [^4_4][^4_2] |
| SRE pour chaque bâtiment | **Non / très limité** | RegBL, certifications énergétiques | La SRE n’est pas une donnée de référence systématique du RegBL. [^4_1][^4_2] |

## 1. Habitation et logements

Il faut bien séparer deux unités :

- **Bâtiment d’habitation** : identifié par `EGID` dans le RegBL.
- **Logement** : identifié par `EWID` ; un bâtiment peut contenir un ou plusieurs logements.[^4_2][^4_4]

Ajoutez donc deux lignes ou deux colonnes distinctes :


| Indicateur | Unité | Source | Champ utile |
| :-- | :-- | :-- | :-- |
| Nouveaux bâtiments d’habitation | Bâtiment | RegBL / StatBL | `EGID`, statut « achevé », année de construction `GBAUJ` |
| Nouveaux logements | Logement | RegBL / OFS | `EWID`, statut « achevé », année de construction du logement |
| Logements dans les nouveaux bâtiments | Logement | RegBL | Lien `EWID` → `EGID` |

Le RegBL enregistre le statut et la date de construction/démolition tant pour les bâtiments que pour les logements, ce qui permet de compter les nouveaux logements sans les confondre avec les nouveaux bâtiments.[^4_10][^4_2]

## 2. Nombre de pièces

**Oui, c’est disponible**, et la définition est fédérale, donc normalement homogène entre cantons. Dans le RegBL, le nombre de pièces comprend les pièces d’habitation formant le logement : séjours, chambres, chambres d’enfants, etc.[^4_3]

Ne comptent pas comme pièces :

- cuisine ou cuisinette ;
- salle de bains, douche, toilettes ;
- réduits, corridors, vérandas ;
- demi-pièces ;
- pièces d’habitation situées hors du logement.[^4_7][^4_3]


### Tableau à ajouter

| Année | Canton | Nombre de nouveaux logements | 1 pièce | 2 pièces | 3 pièces | 4 pièces | 5 pièces | 6 pièces ou plus |
| :-- | :-- | --: | --: | --: | --: | --: | --: | --: |
| 2000 | ZH |  |  |  |  |  |  |  |
| 2000 | GE |  |  |  |  |  |  |  |

Une table PX Web de l’OFS permet déjà de croiser les logements selon le canton, le nombre de pièces, le mode d’utilisation et d’autres caractéristiques. Genève publie aussi des ventilations par nombre de pièces, de 1 pièce à 6 pièces ou plus.[^4_11][^4_7]

### Interprétation cantonale

Vous n’avez normalement **pas besoin d’une conversion cantonale** pour le nombre de pièces : la définition RegBL est nationale. En revanche, soyez prudent sur trois points :

1. **Le séjour compte comme une pièce** : un « 3 pièces » comprend généralement séjour + deux chambres, pas trois chambres.
2. **La cuisine ne compte pas** : un appartement avec cuisine séparée et deux chambres est un 3 pièces si le séjour est compté, sinon un 2 pièces selon la pratique d’enregistrement ; la règle RegBL exclut explicitement la cuisine du décompte.[^4_3]
3. **Les demi-pièces sont exclues** : elles ne doivent donc pas être converties en 0,5 pièce dans vos totaux.[^4_7][^4_3]

Pour les comparaisons historiques ou entre cantons, vérifiez surtout la **qualité de saisie** et les mises à jour du RegBL, plutôt qu’une différence de définition.[^4_12]

## 3. Densification et remplacement

C’est le point le plus difficile. Le RegBL enregistre la démolition d’un bâtiment avec son année de démolition `GABBJ` et le statut `GSTAT = 1007`, mais il ne fournit pas, à ma connaissance, un champ standard reliant automatiquement un nouveau bâtiment au bâtiment démoli qu’il remplace.[^4_8][^4_1]

### Ce qui est faisable

| Question | Méthode | Données nécessaires |
| :-- | :-- | :-- |
| Le nouveau bâtiment remplace-t-il une démolition ? | Analyse spatio-temporelle : bâtiment démoli sur la même parcelle ou emprise proche, peu avant la construction | RegBL, coordonnées, cadastre, parcelles |
| Le bâtiment est-il construit en zone déjà urbanisée ? | Superposition avec le périmètre bâti, les zones à bâtir et l’occupation du sol antérieure | Cadastre, zones d’affectation, MOcad, Orthophotos, swissTLM3D |
| Le projet participe-t-il à la densification ? | Comparaison avant/après : nombre de logements, SRE/surface, volume ou emprise au sol | RegBL, cadastre, données du projet |

### Variable recommandée

Ajoutez une colonne qualitative :


| Valeur | Définition opérationnelle |
| :-- | :-- |
| Remplacement | Un bâtiment a été démoli sur la même parcelle ou une emprise largement chevauchante dans les 1 à 5 années précédentes. |
| Densification sur site bâti | Construction sur une parcelle déjà urbanisée, sans démolition complète, avec augmentation des logements, de la surface ou du volume. |
| Extension / transformation | Modification d’un bâtiment existant, sans création d’un nouveau bâtiment. |
| Nouvelle urbanisation | Construction sur une parcelle précédemment non bâtie ou hors du périmètre bâti antérieur. |

Cette classification n’est pas officielle : elle doit être construite par vous à partir du croisement RegBL + cadastre + historique géospatial.

## 4. Nombre de niveaux

**Oui.** Le RegBL contient le nombre d’étages comme information structurelle du bâtiment.[^4_6][^4_1][^4_2]

Ajoutez :


| Année | Canton | Type | Bâtiments | Nombre moyen d’étages | 1 étage | 2 étages | 3 étages | 4 étages | 5 étages et plus |
| :-- | :-- | :-- | --: | --: | --: | --: | --: | --: | --: |

Attention : « nombre d’étages » ne signifie pas automatiquement « hauteur du bâtiment ». Un bâtiment avec niveaux en attique, sous-sol ou étages de hauteurs variables peut avoir une hauteur très différente pour un même nombre d’étages.[^4_1][^4_2]

## 5. Bâtiments démolis

**Oui pour l’essentiel.** Le RegBL permet d’identifier les bâtiments démolis grâce au statut « démoli » et à l’année de démolition.[^4_2][^4_8][^4_1]


| Caractéristique d’un bâtiment démoli | Disponible ? | Où |
| :-- | :-- | :-- |
| Canton / commune | Oui | RegBL |
| Année de démolition | Oui | `GABBJ` |
| Catégorie de bâtiment | Oui | RegBL |
| Surface et volume | Oui | RegBL, dimensions du bâtiment |
| Nombre d’étages | Oui | RegBL |
| Nombre de logements | Oui | RegBL, via les `EWID` liés à l’`EGID` |
| Nombre de pièces par logement | Oui | RegBL, niveau logement |
| Surface utile | Souvent oui, selon la variable enregistrée | RegBL |
| **SRE** | **Généralement non** | Non standard dans le RegBL |

Le service web du RegBL enregistre explicitement la démolition avec l’année de démolition, puis applique le statut « démoli » au bâtiment et « éliminé » à ses entrées et logements.[^4_8]

### Tableau démolitions

| Année | Canton | Type | Bâtiments démolis | Logements perdus | Surface | Volume | Étages moyens |
| :-- | :-- | :-- | --: | --: | --: | --: | --: |
| 2000 | ZH | Habitation |  |  |  |  |  |
| 2000 | ZH | Bureaux |  |  |  |  |  |
| 2000 | ZH | Écoles |  |  |  |  |  |

## 6. Formes géométriques

C’est possible, mais pas avec le RegBL seul.


| Élément géométrique | Disponible ? | Source recommandée |
| :-- | :-- | :-- |
| Emprise au sol 2D | Oui | Cadastre, swissTLM3D, swissBUILDINGS3D, géodonnées cantonales |
| Forme du polygone au sol | Oui | Mêmes sources ; forme brute disponible, classification automatique à créer |
| Nombre de niveaux | Oui | RegBL |
| Hauteur totale | Partiellement | swissBUILDINGS3D, modèles 3D cantonaux, parfois MNS/MNT |
| Volume | Oui | RegBL, champ `GVOL` [^4_1] |
| Forme 3D complète | Partiellement | swissBUILDINGS3D et modèles urbains 3D cantonaux |

Le RegBL fournit les coordonnées, les dimensions, le volume et le nombre d’étages, mais pas une géométrie détaillée du bâtiment ni une classification de sa forme.[^4_4][^4_6][^4_1]

### Classification proposée

Vous pouvez créer une typologie simple :


| Forme | Règle indicative |
| :-- | :-- |
| Rectangulaire / barre | Rapport longueur/largeur élevé, polygone proche d’un rectangle |
| En L / en U | Polygone concave avec une ou plusieurs rentrées |
| Compact / pavillonnaire | Rapport longueur/largeur proche de 1, faible concavité |
| Complexe | Plusieurs ailes, cour intérieure ou polygone très découpé |

Ajoutez aussi :

- surface d’emprise au sol, en m² ;
- nombre d’étages ;
- hauteur totale, en m ;
- volume, en m³ ;
- indice de compacité : volume / surface d’emprise.


## 7. Point critique : la SRE

La **SRE** n’est pas une donnée de référence universelle du RegBL. Le RegBL contient des surfaces et le volume du bâtiment, mais la SRE relève plutôt des certifications énergétiques, des registres énergétiques cantonaux ou des données Minergie.[^4_1][^4_2]

Recommandation pour votre tableau :


| Colonne | À remplir avec |
| :-- | :-- |
| Surface RegBL | Surface disponible dans le RegBL, à documenter précisément |
| Surface utile | Si disponible |
| SRE | Uniquement si la source le précise explicitement |
| SRE estimée | À éviter, sauf si vous documentez la méthode et les coefficients |

Ne mettez pas « SRE » par défaut pour les bâtiments démolis : ce serait probablement une reconstruction estimée, pas une donnée observée.[^4_2][^4_1]

## Structure finale recommandée

Je vous conseille **trois tables liées**, plutôt qu’un seul tableau gigantesque :

### Table A — Bâtiments

`annee`, `canton`, `commune`, `EGID`, `type_batiment`, `statut`, `evenement` (construction / démolition), `nombre_etages`, `surface`, `volume`, `coordonnees`, `source`.

### Table B — Logements

`annee`, `canton`, `EWID`, `EGID`, `statut`, `evenement`, `nombre_pieces`, `surface_logement`, `type_habitation`.

### Table C — Contexte foncier et morphologie

`EGID`, `parcelle`, `emprise_sol_m2`, `hauteur_m`, `forme_2d`, `densification`, `remplacement`, `zone_avant_construction`, `source_geomatique`.

Cette structure permet de compter correctement :

- les nouveaux **bâtiments** ;
- les nouveaux **logements** ;
- les logements par nombre de pièces ;
- les démolitions ;
- la densification ;
- la morphologie urbaine.[^4_4][^4_3][^4_1][^4_2]

<span style="display:none">[^4_13][^4_14][^4_15][^4_16][^4_17]</span>

<div align="center">⁂</div>

[^4_1]: https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/bericht_gebaeude_und_wohnungsstammdaten.pdf.download.pdf/Rapport%20Donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence%20des%20b%C3%A2timents%20et%20des%20logements%20-%20D%C3%A9finitions,%20gestion%20des%20donn%C3%A9es,%20processus,%20contenu%20des%20registres%20et%20d%C3%A9finition%20des%20donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence.pdf

[^4_2]: https://www.housing-stat.ch/fr/docs/levels.html

[^4_3]: https://www.regbl.admin.ch/files/882-2200.pdf

[^4_4]: https://www.bfs.admin.ch/bfsstatic/dam/assets/214359/master

[^4_5]: https://www.bfs.admin.ch/bfsstatic/dam/assets/349802/master

[^4_6]: https://www.bfs.admin.ch/bfs/fr/home/statistiques/construction-logement/enquetes/gws2009/questions-frequentes.html

[^4_7]: https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0903020000_102/px-x-0903020000_102/px-x-0903020000_102.px

[^4_8]: https://www.bfs.admin.ch/bfsstatic/dam/assets/214349/master

[^4_9]: https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/gebaudewohnungsstammdaten.pdf.download.pdf/Données de référence des bâtiments et des logements.pdf

[^4_10]: https://www.lexfind.ch/tolv/253175/fr

[^4_11]: https://sitg.ge.ch/donnees/ocs-batlog-ssecteur

[^4_12]: https://www.bfs.admin.ch/bfsstatic/dam/assets/348194/master

[^4_13]: https://www.bfs.admin.ch/bfs/fr/home/statistiques/construction-logement/logements/logements-locataires.html

[^4_14]: https://www.fr.ch/deef/ssd/statistiques-par-themes/logements

[^4_15]: https://statistique.ge.ch/domaines/09/09_02/methodologie.asp

[^4_16]: https://www.housing-stat.ch/files/181120_GA_FR.pdf

[^4_17]: https://www.housing-stat.ch/fr/docs/whatsnew.html


---

# Il faut distinguer surface SRE et surface utile dans deux colonnes et selon la source utilisée. Pour les trois tables proposées et chacune de leurs catégories, indique la source de la donnée. Est-ce qu'il existe d'autres classes de bâtiments que ceux-là: "Regroupement par classe de bâtiment RegBL

Logement : classes 1110, 1121, 1122 et 1130.
Bureaux / commerce : classes 1220 et 1230.
Enseignement : classe 1263."
?

Oui. Votre regroupement est correct pour les trois grandes familles, mais il est **incomplet** : le RegBL utilise la classification Eurostat des classes de bâtiments, avec des codes `GKLAS` allant de **1110 à 1274**.[^5_1][^5_2]

## 1. SRE et surface utile : deux colonnes distinctes

Il faut effectivement séparer les deux indicateurs, car ils ne mesurent pas la même chose et n’ont pas la même couverture.


| Colonne | Définition | Source principale | Disponibilité |
| :-- | :-- | :-- | :-- |
| `surface_utile_m2` | Surface effectivement utilisable du bâtiment ou du logement | RegBL — dimensions du bâtiment | Bonne couverture pour les bâtiments et logements enregistrés. [^5_3][^5_4] |
| `surface_reference_energetique_m2` | Surface de référence énergétique, indicateur normalisé pour l’analyse énergétique | RegBL — module « Énergie » ; certificats énergétiques ; Minergie | Partielle : la SRE figure dans le catalogue RegBL, mais elle n’est pas systématiquement renseignée pour tous les bâtiments. [^5_5][^5_4] |

### Règle à appliquer

- Ne jamais fusionner les deux colonnes.
- Ajouter une colonne `source_surface` avec les valeurs : `RegBL_surface_utile`, `RegBL_SRE`, `certificat_energetique`, `Minergie`, `estimation`.
- Ajouter une colonne `qualite_donnee` : `observée`, `déclarée`, `estimée`, `manquante`.
- Pour les bâtiments démolis, la surface utile peut exister dans le RegBL, mais la SRE sera souvent absente.[^5_3][^5_4][^5_5]


## 2. Sources par table

### Table A — Bâtiments

| Champ | Source | Remarque |
| :-- | :-- | :-- |
| `EGID` | RegBL | Identifiant fédéral du bâtiment. [^5_6][^5_4] |
| `annee_construction` | RegBL | Champ `GBAUJ`. [^5_3][^5_4] |
| `annee_demolition` | RegBL | Champ `GABBJ`. [^5_3][^5_7][^5_4] |
| `statut_batiment` | RegBL | Projeté, achevé, démoli. [^5_4][^5_8] |
| `canton`, `commune` | RegBL | Localisation administrative. [^5_6] |
| `categorie_batiment` `GKAT` | RegBL | Habitation, sans habitation, objet divers, etc. [^5_9][^5_10] |
| `classe_batiment` `GKLAS` | RegBL | Classification Eurostat, codes 1110–1274. [^5_1][^5_2] |
| `nombre_etages` | RegBL | Information structurelle du bâtiment. [^5_3][^5_11][^5_4] |
| `surface_utile_m2` | RegBL | Dimensions du bâtiment. [^5_3][^5_4] |
| `surface_reference_energetique_m2` | RegBL Énergie / certificat énergétique / Minergie | Couverture partielle. [^5_5] |
| `volume_m3` | RegBL | Volume du bâtiment. [^5_3][^5_4] |
| `coordonnees` | RegBL / MOcad | Position du bâtiment. [^5_6] |
| `emprise_sol_m2` | Cadastre, swissTLM3D, swissBUILDINGS3D | Géodonnées, pas RegBL. |
| `hauteur_m` | swissBUILDINGS3D, modèles 3D cantonaux | Pas un attribut standard du RegBL. |
| `forme_2d` | Cadastre / swissBUILDINGS3D | Polygone à classifier vous-même. |

### Table B — Logements

| Champ | Source | Remarque |
| :-- | :-- | :-- |
| `EWID` | RegBL | Identifiant fédéral du logement. [^5_6][^5_4] |
| `EGID` | RegBL | Lien vers le bâtiment. [^5_6][^5_4] |
| `statut_logement` | RegBL | Projeté, achevé, démoli. [^5_8] |
| `annee_construction_logement` | RegBL | Permet de compter les nouveaux logements. [^5_4] |
| `nombre_pieces` | RegBL | Définition fédérale ; cuisine, salle de bains, réduits et demi-pièces exclus. [^5_12][^5_13] |
| `surface_utile_logement_m2` | RegBL | Surface du logement. [^5_14][^5_4] |
| `surface_reference_energetique_m2` | RegBL Énergie / certificat / Minergie | Généralement au niveau du bâtiment, pas toujours au niveau du logement. [^5_5] |
| `mode_utilisation` | RegBL / OFS | Occupé, vacant, etc. [^5_12] |

### Table C — Contexte foncier et morphologie

| Champ | Source | Remarque |
| :-- | :-- | :-- |
| `parcelle` | Cadastre / Registre foncier cantonal | Nécessaire pour relier bâtiment et parcelle. |
| `zone_a_batir` | Plans d’affectation cantonaux / communaux | Permet de distinguer zone à bâtir, zone agricole, etc. |
| `occupation_avant_construction` | MOcad, swissTLM3D, Orthophotos historiques | Nécessaire pour distinguer site déjà bâti et nouvelle urbanisation. |
| `remplacement` | RegBL + cadastre + analyse spatio-temporelle | Pas de lien standard démolition → nouvelle construction dans le RegBL. [^5_3][^5_7] |
| `densification` | RegBL + cadastre + comparaison avant/après | À construire : variation de logements, surface ou volume. |
| `emprise_sol_m2` | Cadastre / swissBUILDINGS3D | Surface du polygone au sol. |
| `hauteur_m` | swissBUILDINGS3D / modèle 3D cantonal | Hauteur du modèle, pas toujours hauteur réglementaire. |
| `forme_2d` | Calcul sur le polygone cadastral | Classification à définir. |

## 3. Classes RegBL : votre liste est incomplète

Votre regroupement couvre bien l’habitat courant, les bureaux/commerces et les écoles, mais il omet notamment les hôtels, les bâtiments industriels, les entrepôts, les bâtiments de transport, la santé, les bâtiments agricoles, sportifs, culturels et les constructions particulières.[^5_2][^5_15][^5_1]


| Regroupement proposé | Codes `GKLAS` | Signification confirmée |
| :-- | :-- | :-- |
| **Habitation** | 1110 | Bâtiment d’un logement / maison individuelle. [^5_16][^5_15] |
|  | 1121 | Bâtiment de deux logements. [^5_15][^5_17] |
|  | 1122 | Bâtiment de trois logements ou plus. [^5_15][^5_17] |
|  | 1130 | Résidences pour communautés / habitation collective. [^5_1][^5_15] |
|  | 1212 | Résidences mobiles / mobil-homes. [^5_15][^5_17] |
| **Hébergement** | 1211 | Hôtels et bâtiments similaires. [^5_1][^5_15] |
| **Bureaux / commerce** | 1220 | Bureaux. [^5_1] |
|  | 1230 | Bâtiments commerciaux. [^5_1][^5_18] |
| **Industrie / logistique** | 1251 | Bâtiments industriels. [^5_1][^5_18] |
|  | 1252 | Entrepôts. [^5_15] |
| **Enseignement** | 1263 | Bâtiments scolaires. [^5_1][^5_15] |
| **Santé / social** | 1261, 1262, 1264, 1265 | Autres bâtiments publics et d’équipement collectif ; libellés exacts à prendre dans le catalogue. [^5_1][^5_15] |
| **Transports / communication** | 1241, 1242 | Bâtiments de transport et communication. [^5_1][^5_15] |
| **Autres usages** | 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278 | Bâtiments agricoles, sportifs, culturels, techniques et autres. [^5_1][^5_15] |
| **Cas particuliers** | 1231 | Autre classe commerciale / technique figurant au catalogue. [^5_15] |
|  | 1010 | Habitations provisoires : catégorie `GKAT`, pas classe `GKLAS`. [^5_10][^5_17] |
|  | 1020, 1030, 1040, 1060, 1080 | Catégories `GKAT`, pas classes `GKLAS`. [^5_10][^5_17] |

## 4. Correction importante : GKAT et GKLAS

Il faut distinguer deux variables :


| Variable | Rôle | Exemples |
| :-- | :-- | :-- |
| `GKAT` — catégorie de bâtiment | Grand type structurel | 1010 habitations provisoires, 1020 bâtiments exclusivement à usage d’habitation, 1030 autres bâtiments d’habitation, 1040 bâtiments partiellement à usage d’habitation, 1060 bâtiments sans usage d’habitation, 1080 constructions particulières. [^5_10][^5_17] |
| `GKLAS` — classe de bâtiment | Classification Eurostat détaillée | 1110, 1121, 1122, 1130, 1211, 1220, 1230, 1251, 1263, etc. [^5_1][^5_2] |

Votre regroupement « Logement : 1110, 1121, 1122, 1130 » est donc une agrégation de classes `GKLAS`, pas une catégorie `GKAT`.[^5_15][^5_17][^5_1]

## 5. Regroupements recommandés

Pour un tableau lisible, je suggère ces macro-catégories :


| Macro-catégorie | Codes `GKLAS` |
| :-- | :-- |
| Logement individuel | 1110 |
| Logement collectif | 1121, 1122 |
| Habitation collective / communautaire | 1130 |
| Hébergement touristique | 1211 |
| Hébergement temporaire / mobile | 1212 |
| Bureaux | 1220 |
| Commerce | 1230, 1231 |
| Industrie et logistique | 1251, 1252 |
| Enseignement | 1263 |
| Santé et social | 1261, 1262, 1264, 1265 |
| Transports et communication | 1241, 1242 |
| Agriculture | 1271 et codes agricoles associés |
| Sport, culture, loisirs | Codes 127x concernés |
| Bâtiments techniques et autres | Codes 127x restants |

## 6. Où obtenir la liste officielle complète

La liste complète et les libellés officiels en français se trouvent dans :

- le **catalogue des caractères du RegBL** de l’OFS ;[^5_19]
- le fichier de codes téléchargeable `kodes_codes_codici.csv`, mis à disposition dans les données publiques du RegBL ;[^5_20]
- l’aide RegBL « Quelle classe de bâtiment saisir ? », utile pour trancher les cas ambigus, par exemple industrie versus commerce.[^5_18]

Pour votre tableau, conservez toujours le code `GKLAS` brut dans une colonne, puis créez une colonne séparée `macro_categorie`. Cela évite de perdre l’information lors des regroupements.[^5_1][^5_20]

<span style="display:none">[^5_21][^5_22][^5_23]</span>

<div align="center">⁂</div>

[^5_1]: https://www.vd.ch/fileadmin/user_upload/organisation/dinf/sit/fichiers_pdf/Catalogue_caracteres_v35.pdf

[^5_2]: https://www.bfs.admin.ch/bfsstatic/dam/assets/214340/master

[^5_3]: https://www.bk.admin.ch/dam/bk/fr/dokumente/dti/themen/architektur/Stammdatenverwaltung/bericht_gebaeude_und_wohnungsstammdaten.pdf.download.pdf/Rapport%20Donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence%20des%20b%C3%A2timents%20et%20des%20logements%20-%20D%C3%A9finitions,%20gestion%20des%20donn%C3%A9es,%20processus,%20contenu%20des%20registres%20et%20d%C3%A9finition%20des%20donn%C3%A9es%20de%20r%C3%A9f%C3%A9rence.pdf

[^5_4]: https://www.housing-stat.ch/fr/docs/levels.html

[^5_5]: https://www.regbl.admin.ch/files/170920_GA_FR.pdf

[^5_6]: https://www.bfs.admin.ch/bfsstatic/dam/assets/214359/master

[^5_7]: https://www.bfs.admin.ch/bfsstatic/dam/assets/214349/master

[^5_8]: https://www.lexfind.ch/tolv/253175/fr

[^5_9]: https://dam-api.bfs.admin.ch/hub/api/dam/assets/22686123/master

[^5_10]: https://www.ne.ch/autorites/DDTE/SGRF/mensuration/Documents/Directives/HarmRegBL_MO_CantonNE.pdf

[^5_11]: https://www.bfs.admin.ch/bfs/fr/home/statistiques/construction-logement/enquetes/gws2009/questions-frequentes.html

[^5_12]: https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0903020000_102/px-x-0903020000_102/px-x-0903020000_102.px

[^5_13]: https://www.regbl.admin.ch/files/882-2200.pdf

[^5_14]: https://www.bfs.admin.ch/bfsstatic/dam/assets/348194/master

[^5_15]: https://www.regbl.admin.ch/files/883-2200.pdf

[^5_16]: https://www.vd.ch/fileadmin/user_upload/organisation/dinf/sit/fichiers_xls/GWRCodes_20050624.xls

[^5_17]: https://www.regbl.admin.ch/files/Nouveautés_CC42.docx

[^5_18]: https://www.housing-stat.ch/fr/help/faq/gklas.html

[^5_19]: https://www.bfs.admin.ch/asset/fr/7008786

[^5_20]: https://www.regbl.admin.ch/fr/madd/public.html

[^5_21]: https://www.regbl.admin.ch/files/Listes_cantons/Listes_JU.xlsx

[^5_22]: https://www.housing-stat.ch/fr/help/42.html

[^5_23]: https://www.housing-stat.ch/fr/docs/whatsnew.html

