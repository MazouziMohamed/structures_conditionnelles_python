# L'énoncé de l'exercice
''' Les produits vendus dans un magasin sont classés en trois catégories de
point de vue TVA : A=7%, B=20% et C=25%. Ecrivez un programme qui
calcule le prix TTC d’un produit connaissant son prix hors taxe et sa catégorie. '''
# la solution corrigée de l'exercice
print('+' + '-'*10 + 'TVA-Catégorie' + '-'*10 + '+')
print('A = 7% et B = 20% et C = 25%')
print('-'*35)
tva = input('Veuillez entrer le tva (A ou B ou C) : ')
prix_hors_taxe = float(input('Veuillez entrer le prix hors taxe : '))
if tva == 'A' :
    prix_ttc = prix_hors_taxe * 1.07
elif tva == 'B' :
    prix_ttc = prix_hors_taxe * 1.2
elif tva == 'C' :
    prix_ttc = prix_hors_taxe * 1.25
else :
    print('Erreur de saisie, la catégorie n\'existe pas.')
    exit()
print('Le prix TTC est :', prix_ttc, 'DH')
