# L'énoncé de l'exercice
''' Ecrire un programme qui demande deux nombres entiers et l'une des
opérateurs suivant : +, -, *, / puis effectue l'opération correspond et
affiche le résultat de cette opération. '''
# la solution corrigée de l'exercice
print('+-------------------Opérateurs-------------------+')
print('1 : Addition')
print('2 : Soustraction')
print('3 : Multiplication')
print('4 : Division')
print('+------------------------------------------------+')
choix = int(input('Veuillez entrer votre choix (1 ou 2 ou 3 ou 4) : '))
premier_entier = int(input('Veuillez entrer le premier entier : '))
deuxieme_entier = int(input('Veuillez entrer le deuxième entier : '))
if choix == 1 :
    print(premier_entier, '+', deuxieme_entier, '=', premier_entier + deuxieme_entier)
elif choix == 2 :
    print(premier_entier, '-', deuxieme_entier, '=', premier_entier - deuxieme_entier)
elif choix == 3 :
    print(premier_entier, '*', deuxieme_entier, '=', premier_entier * deuxieme_entier)
elif choix == 4 :
    if deuxieme_entier != 0 :
        print(premier_entier, '/', deuxieme_entier, '=', premier_entier / deuxieme_entier)
    else :
        print('La division par 0 est impossible.')
else :
    print('Erreur de saisie le choix.')
