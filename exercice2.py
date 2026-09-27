# L'énoncé de l'exercice
''' Ecrire un programme qui échange les contenus de deux données
numérique si elles sont de même signe, sinon il met la somme des deux
dans la première donnée et leur produit dans la seconde. '''
# la solution corrigée de l'exercice
A = float(input('Veuillez entrer la valeur de A : '))
B = float(input('Veuillez entrer la valeur de B : '))
print('Avant : A =', A, 'B =', B)
if A * B > 0 :
    A, B = B, A
else :
    A, B = A + B, A * B
print('Après : A =', A, 'B =', B)