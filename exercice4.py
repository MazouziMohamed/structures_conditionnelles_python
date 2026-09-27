# L'énoncé de l'exercice
''' Ecrire un programme qui demore l’âge d’un enfant à l’utilisateur.
Ensuite, il l’informe de sa catégorie : "Poussin" de 6 à 7 ans, "Pupille" de 8
à 9 ans, "Minime" de 10 à 11 ans, "Cadet" après 12 ans. '''
# la solution corrigée de l'exercice
age_enfant = int(input("Veuillez entrer l'âge de l'enfant : "))
if age_enfant >= 6 and age_enfant <= 7 :
    categorie_enfant = 'poussin'
elif age_enfant >= 8 and age_enfant <= 9 :
    categorie_enfant = 'pupille'
elif age_enfant >= 10 and age_enfant <= 11 :
    categorie_enfant = 'minime'
elif age_enfant >= 12 and age_enfant <= 17:
    categorie_enfant = 'cadet'
else :
    categorie_enfant = "n'existe pas"
print("La catégorie de l'enfant est :", categorie_enfant)