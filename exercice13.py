# L'énoncé de l'exercice
''' Ecrire un programme qui demande à l'utilisateur d'entrer un caractère
et vérifie si le caractère donné est un alphabet, un chiffre
ou un caractère spécial. '''
# la solution corrigée de l'exercice
caractere = input('Veuillez entrer un caractère : ')
temporaire = ord(caractere)
if 48 <= temporaire <= 57 :
    print('le caractère donné est un chiffre.')
elif 65 <= temporaire <= 90 or 97 <= temporaire <= 122 :
    print('le caractère donné est un alphabet.')
else :
    print('le caractère donné est un caractère spécial.')