# L'énoncé de l'exercice
''' Ecrire un programme qui vérifier si un nombre est pair ou impair '''
# la solution corrigée de l'exercice
nombre_entier = int(input('Veuillez entrer un nombre entier : '))
if nombre_entier % 2 == 0 :
    print(nombre_entier, 'est un nombre pair.')
else :
    print(nombre_entier, 'est un nombre impair.')