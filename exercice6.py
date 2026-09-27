# L'énoncé de l'exercice
''' Ecrire un programme qui affiche la ou les solutions d’une équation du
second degré de la forme ax² + bx + c. '''
# la solution corrigée de l'exercice
from math import sqrt
a = float(input('Veuillez entrer la valeur du coefficient a : '))
b = float(input('Veuillez entrer la valeur du coefficient b : '))
c = float(input('Veuillez entrer la valeur du coefficient c : '))
if a == 0 :
    if b == 0 :
        if c == 0 :
            print("L'ensemble des solutions est : l'ensemble des nombres réels")
        else :
            print("L'ensemble des solutions est : l'ensemble vide")
    else :
        racine_double = -c / b
        print("L'ensemble des solutions est : S = {", racine_double, "}")
else :
    delta = b**2 - 4*a*c
    if delta > 0 :
        premiere_solution = (-b - sqrt(delta)) / (2*a)
        deuxieme_solution = (-b + sqrt(delta)) / (2*a)
        print("L'ensemble des solutions est : S = {", premiere_solution, ";", deuxieme_solution, "}")
    elif delta == 0 :
        racine_double = -b / (2*a)
        print("L'ensemble des solutions est : S = {", racine_double, "}")
    else :
        print("L'ensemble des solutions est : l'ensemble vide")