# Détection de contraintes
## Dépendances
- numpy
- pandas

## Run
Lancer le fichier `check_contraints.py` pour afficher les contraintes qui ne sont pas respectées

## Fichier d'entrée
`Soutenances M1 janvier 2020 - Contraintes.xlsx`: Planning avec des violations de contraintes ajoutées manuellement
`Soutenances M1 janvier 2020.xlsx`: Planning avec les violations de contraintes corrigées en fonction des résultats du programme

# Format du fichier d'entrée excel
- Nom du candidat 
- Prénom du candidat
- Email du candidat
- Entreprise du candidat
- Date: YYYY.mm.dd
- Heure de début de soutenance: HH:MM
- Heure de fin de soutenance: HH:MM
- Numéro du jury
- Salle
- Nom/Prénom du président du jury
- Nom/Prénom du tuteur Universitaire

## Information manquante nécéssaire a la génération d'un planing
- Nom prénom du tuteur académique
- Nom prénom du tuteur de l'entreprise
- Plage horaire disponible
- Durées des soutenances
- Les disponibilités/indisponibilités des tuteurs (entreprise et académique)
- Les salles disponibles (nombre et noms des salles)
