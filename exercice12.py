# L'énoncé de l'exercice
''' Ecrire un programme qui demande à l'utilisateur de saisir une année
et qui vérifie s'elle est bissextile (366 jours) ou non. '''
# la solution corrigée de l'exercice
annee = int(input('Veuillez entrer une année : '))
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0 :
    print(annee, 'est une année bissextile.')
else :
    print(annee, 'n\'est pas une année bissextile.')