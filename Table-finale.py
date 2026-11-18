import pandas as pd


# Chargement des bases


personne = pd.read_parquet(
    "s3://catioui/personne_activite_clean.parquet"
)

savoirfaire = pd.read_parquet(
    "s3://catioui/savoirfaire_clean.parquet"
)


# Jointure sur Identifiant PP


table_finale = pd.merge(
    personne,
    savoirfaire,
    on="Identifiant PP",
    how="left"
)

print("Dimensions de la table finale :")
print(table_finale.shape)

print("\n10 premières lignes :")
print(table_finale.head(10).to_string())

# Regroupement par commune


offre_commune = (
    table_finale
    .groupby(
        [
            "Code commune (coord. structure)",
            "Libellé commune (coord. structure)"
        ]
    )
    .agg(
        nb_professionnels=("Identifiant PP", "nunique")
    )
    .reset_index()
)

print("\nDimensions de la table par commune :")
print(offre_commune.shape)

print("\n10 premières communes :")
print(offre_commune.head(10).to_string())


# Sauvegarde


offre_commune.to_parquet(
    "s3://catioui/offre_soins_commune.parquet",
    index=False
)

print("\n Fichier enregistré : offre_soins_commune.parquet")