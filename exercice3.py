# L'énoncé de l'exercice
''' Un magasin facture 0,30 dh les dix premières photocopies, 0,25 dh les
vingt suivantes et 0,20 dh au-delà. Ecrire un programme qui demande à
l’utilisateur le nombre de photocopies effectuées et qui affiche la facture
correspondante. '''
# la solution corrigée de l'exercice
nombre_photocopies_effectuees = int(input('Veuillez entrer le nombre de photocopies que vous voulez effectuer : '))
if nombre_photocopies_effectuees <= 10 :
    facture = nombre_photocopies_effectuees * 0.30
elif nombre_photocopies_effectuees <= 30 :
    facture = 10 * 0.30 + (nombre_photocopies_effectuees - 10) * 0.25
else :
    facture = 10 * 0.30 + 20 * 0.25 + (nombre_photocopies_effectuees - 30) * 0.20
print('La facture est :', facture, 'DH')