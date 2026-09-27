# L'énoncé de l'exercice
''' Ecrire un programme qui demande à l'utilisateur de saisir un nombre puis qui en fonction du nombre saisi :
- 6 : affiche « le personnage va à droite ».
- 4 : affiche « le personnage va à gauche ».
- 8 : affiche « le personnage va en haut ».
- 2 : affiche « le personnage va en bas ».
- dans le cas d'un autre caractère, affiche : « erreur de saisie, le personnage ne bouge pas ». '''
# la solution corrigée de l'exercice
nombre_saisi = int(input('Veuillez entrer un nombre : '))
if nombre_saisi == 6 :
    print('Le personnage va à droite.')
elif nombre_saisi == 4 :
    print('Le personnage va à gauche.')
elif nombre_saisi == 8 :
    print('Le personnage va en haut.')
elif nombre_saisi == 2 :
    print('Le personnage va en bas.')
else :
    print('Erreur de saisie, le personnage ne bouge pas.')