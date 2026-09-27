# L'énoncé de l'exercice
''' Ecrire un programme permettant de saisir trois notes (sur 20) d'un
étudiant, calculant sa moyenne et affichant cette moyenne avec la
mention ("Très bien" à partir de 16, "Bien" entre 14 et 16, "Assez bien"
entre 12 et 14, "Passable" entre 10 et 12, "Insuffisant" en dessous de 10)
PS : On suppose que l'étudiant va saisir des notes comprises entre 0 et 20. '''
# la solution corrigée de l'exercice
note1 = float(input('Veuillez entrer la première note : '))
note2 = float(input('Veuillez entrer la deuxième note : '))
note3 = float(input('Veuillez entrer la troisième note : '))
moyenne_notes = (note1 + note2 + note3) / 3
if moyenne_notes >= 16 :
    mention = 'Très bien'
elif moyenne_notes >= 14 :
    mention = 'Bien'
elif moyenne_notes >= 12 :
    mention = 'Assez bien'
elif moyenne_notes >= 10 :
    mention = 'Passable'
else :
    mention = 'Insuffisant'
print("La moyenne de l'étudiant est :", moyenne_notes)
print("La mention de l'étudiant est :", mention)