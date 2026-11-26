# Analyse de l'accessibilité aux soins médicaux en France

Ce projet étudie les **inégalités territoriales d'accès aux médecins généralistes en France** à l'échelle communale.

L'objectif est de construire un indicateur d'accessibilité qui ne se limite pas au nombre de médecins présents dans une commune. Il prend également en compte les médecins accessibles dans les communes voisines, les temps de trajet routiers, la population susceptible de solliciter cette offre et la structure par âge de la population.

L'approche est inspirée des indicateurs de type **APL (Accessibilité Potentielle Localisée)** et **E2SFCA**, sans chercher à reproduire exactement l'indicateur officiel de la DREES.

## Données

Le projet mobilise plusieurs sources de données publiques :

- **INSEE**
  - population communale ;
  - structure de la population par âge ;
  - grille communale de densité ;
  - FILOSOFI : niveau de vie médian et taux de pauvreté ;

- **RPPS**
  - professionnels de santé ;
  - identification des médecins généralistes ;
  - communes d'exercice ;

- **FINESS / SYGEN**
  - établissements sanitaires ;
  - capacités hospitalières ;
  - lits et équipements médicaux ;

- **Données géographiques**
  - coordonnées et contours des communes ;
  - temps et distances routières calculés entre communes.

## Construction de l'indicateur

### 1. Offre de médecins généralistes

L'offre médicale est construite à partir du RPPS.

Lorsqu'un médecin exerce dans plusieurs communes, son poids est réparti entre ses différentes communes d'exercice afin d'éviter le double comptage.

Par exemple, un médecin exerçant dans deux communes compte pour `0,5` dans chacune.

### 2. Demande de soins

Deux mesures de la demande sont considérées :

- la population communale brute ;
- une demande standardisée tenant compte de la structure par âge.

Cette seconde mesure permet de tenir compte des différences de besoins potentiels en soins entre les territoires.

### 3. Accessibilité géographique

Les relations entre communes sont construites à partir des temps de trajet routiers.

Les poids utilisés sont :

| Temps de trajet | Poids |
|---|---:|
| ≤ 10 minutes | 1 |
| 10–15 minutes | 2/3 |
| 15–20 minutes | 1/3 |
| > 20 minutes | 0 |

### 4. Indicateur d'accessibilité

Pour chaque commune disposant d'une offre médicale \(j\), on calcule :

\[
R_j =
\frac{O_j}
{\sum_i D_i w_{ij}}
\]

où :

- \(O_j\) représente l'offre de médecins généralistes ;
- \(D_i\) représente la demande de la commune \(i\) ;
- \(w_{ij}\) représente le poids associé au temps de trajet entre les communes.

L'accessibilité d'une commune \(i\) est ensuite :

\[
A_i =
\sum_j R_j w_{ij}
\]

L'indicateur final est exprimé en **médecins généralistes accessibles pour 100 000 habitants**.

Une valeur élevée correspond donc à une meilleure accessibilité potentielle.

## Analyses réalisées

Le projet étudie notamment :

- la distribution nationale de l'accessibilité ;
- les écarts entre densité médicale locale et accessibilité spatiale ;
- les communes sans médecin généraliste bénéficiant néanmoins d'une offre accessible à proximité ;
- les différences entre territoires urbains, intermédiaires et ruraux ;
- le lien avec le niveau de vie ;
- le lien avec le taux de pauvreté ;
- l'effet de la structure par âge ;
- les relations avec l'offre sanitaire et hospitalière ;
- les disparités départementales.

Les résultats sont complétés par des cartes communales, départementales et une carte interactive.

## Organisation du dépôt

```text
.
├── requirements.txt
├── README.md
│
└── src/
    ├── INSEE/
    │   ├── preparation_population.ipynb
    │   ├── preparation_filosofi.ipynb
    │   ├── preparation-grille_densite.ipynb
    │   └── fusion_insee.ipynb
    │
    ├── RPPS/
    │   ├── preparation_personne_activite.ipynb
    │   ├── preparation_savoirfaire.ipynb
    │   └── fusion_rpps_offre_commune.ipynb
    │
    ├── SYGEN_FINESS/
    │   ├── prepa_finess.ipynb
    │   ├── preparation_sygen_2025.ipynb
    │   └── fusion_finess_sygen.ipynb
    │
    ├── fusion/
    │
    ├── Indicateur_dacces/
    │   ├── distances_accessibilité.ipynb
    │   ├── offre_demande.ipynb
    │   ├── Indicateur_finale.ipynb
    │   └── Fusion_finale_et_analyse_stat.ipynb
    │
    ├── Analyses_finales_et_cartes.ipynb
    │
    └── outputs/
        ├── tables/
        ├── figures/
        └── cartes/
```

## Installation

Cloner le dépôt puis installer les dépendances :

```bash
git clone https://github.com/Chaimaa-ui77/Analyse-d-accessibilite-des-soins-medicaux.git

cd Analyse-d-accessibilite-des-soins-medicaux

pip install -r requirements.txt
```

Le projet a principalement été développé sur **SSPCloud / Onyxia**.

## Principaux résultats produits

Les sorties des analyses finales sont enregistrées dans :

```text
src/outputs/
```

avec :

```text
outputs/
├── tables/
├── figures/
└── cartes/
```

La carte interactive est enregistrée sous :

```text
src/outputs/cartes/carte_accessibilite_interactive.html
```

## Limites

L'indicateur construit mesure une **accessibilité potentielle** et non le recours effectif aux soins.

Il ne prend notamment pas directement en compte :

- les délais de rendez-vous ;
- l'acceptation de nouveaux patients ;
- le temps de travail réel des médecins ;
- les préférences individuelles des patients ;
- les déplacements effectivement observés.

Les relations observées entre accessibilité, revenu, pauvreté, âge ou offre hospitalière sont par ailleurs descriptives et ne doivent pas être interprétées comme des relations causales.

## Reproductibilité

Les données intermédiaires volumineuses sont stockées sur SSPCloud/MinIO et sont chargées par les notebooks à partir de leurs emplacements publics lorsque cela est possible.

Les notebooks du dépôt documentent successivement :

1. la préparation des données ;
2. leur harmonisation géographique ;
3. le calcul des temps de trajet ;
4. la construction de l'offre et de la demande ;
5. le calcul de l'indicateur d'accessibilité ;
6. la fusion finale ;
7. les analyses statistiques et cartographiques.
