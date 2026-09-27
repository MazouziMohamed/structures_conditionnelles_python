# L'énoncé de l'exercice
'''Ecrire un programme qui retourne si deux nombres entiers donnés sont
de même signe ou non.'''
# la solution corrigée de l'exercice
premier_entier = int(input('Veuillez entrer le premier entier : '))
deuxieme_entier = int(input('Veuillez entrer le deuxième entier : '))
if premier_entier * deuxieme_entier > 0 :
    print(premier_entier, 'et', deuxieme_entier, 'ont le même signe.')
else :
       print(premier_entier, 'et', deuxieme_entier, 'ont des signes contraires.')