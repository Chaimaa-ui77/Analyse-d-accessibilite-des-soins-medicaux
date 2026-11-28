import pandas as pd


# Chargement de la base


savoirfaire = pd.read_csv(
    "s3://catioui/ps-libreacces-savoirfaire.txt",
    sep="|",
    low_memory=False
)


# Informations sur la base


print("Dimensions de la base :")
print(savoirfaire.shape)

print("\n10 premières lignes :")
print(savoirfaire.head(10).to_string())


# Sélection des colonnes utiles


colonnes_savoirfaire = [
    "Identifiant PP",
    "Libellé profession",
    "Code type savoir-faire",
    "Libellé type savoir-faire",
    "Code savoir-faire",
    "Libellé savoir-faire"
]

savoirfaire_clean = savoirfaire[colonnes_savoirfaire].copy()


# Contrôles après nettoyage


print("\nDimensions après nettoyage :")
print(savoirfaire_clean.shape)

print("\nValeurs manquantes :")
print(savoirfaire_clean.isna().sum())

print("\nNombre de professionnels distincts :")
print(savoirfaire_clean["Identifiant PP"].nunique())

print("\nNombre de savoir-faire distincts :")
print(savoirfaire_clean["Code savoir-faire"].nunique())

print("\nAperçu de la base nettoyée :")
print(savoirfaire_clean.head(10).to_string())


# Sauvegarde de la base traitée


savoirfaire_clean.to_parquet(
    "s3://catioui/savoirfaire_clean.parquet",
    index=False
)

print("\n Base nettoyée enregistrée : savoirfaire_clean.parquet")