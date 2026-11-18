import pandas as pd

#  Chargement de la base

personne = pd.read_csv(
    "s3://catioui/ps-libreacces-personne-activite.txt",
    sep="|",
    low_memory=False
)
#  Informations sur la base


print("Dimensions de la base :")
print(personne.shape)

print("\n10 premières lignes :")
print(personne.head(10).to_string())


# Sélection des colonnes 


colonnes_personne = [
    "Identifiant PP",
    "Libellé profession",
    "Code mode exercice",
    "Libellé mode exercice",
    "Numéro FINESS site",
    "Raison sociale site",
    "Code secteur d'activité",
    "Libellé secteur d'activité",
    "Code commune (coord. structure)",
    "Libellé commune (coord. structure)",
    "Code postal (coord. structure)",
    "Code Département (structure)"
]

personne_clean = personne[colonnes_personne].copy()


#  après netoyage


print("\nDimensions après nettoyage :")
print(personne_clean.shape)

print("\nValeurs manquantes :")
print(personne_clean.isna().sum())

print("\nNombre de professionnels distincts :")
print(personne_clean["Identifiant PP"].nunique())

print("\nNombre de communes distinctes :")
print(personne_clean["Code commune (coord. structure)"].nunique())

print("\nAperçu de la base nettoyée :")
print(personne_clean.head(10).to_string())

# Sauvegarde de la base traitée


personne_clean.to_parquet(
    "s3://catioui/personne_activite_clean.parquet",
    index=False
)

print("\n Base nettoyée enregistrée : personne_activite_clean.parquet")
