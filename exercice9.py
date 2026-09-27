# L'énoncé de l'exercice
''' Ecrire un programme qui demande deux nombres entiers et l'une des
opérateurs suivant : +, -, *, / puis effectue l'opération correspond et
affiche le résultat de cette opération. '''
# la solution corrigée de l'exercice
from rich import print
from rich.align import Align
print(Align.center('+-------------------[bold red]Opérateurs[/bold red]-------------------+'))
print('[bold red]1 : Addition[/bold red]')
print('[bold red]2 : Soustraction[/bold red]')
print('[bold red]3 : Multiplication[/bold red]')
print('[bold red]4 : Division[/bold red]')
print('[bold red]Veuillez entrer votre choix (1 ou 2 ou 3 ou 4) :[/bold red] ', end = '')
choix = int(input())
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