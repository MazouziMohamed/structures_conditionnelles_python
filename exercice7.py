# L'énoncé de l'exercice
''' Les habitants d’une ville paient l’impôt selon les règles suivantes :
- Les hommes de plus de 20 ans paient l’impôt
- Les femmes paient l’impôt si elles ont entre 18 et 35 ans
- Les autres ne paient pas d’impôt
Ecrire un programme qui demande l’âge et le sexe d’un habitant
et affiche si celui-ci est imposable. '''
# la solution corrigée de l'exercice
sexe_habitant = input("Veuillez entrer le sexe de l'habitant (M ou F) : ")
age_habitant = int(input("Veuillez entrer l'âge de l'habitant : "))
if (sexe_habitant == 'M' and age_habitant >= 20) or (sexe_habitant == 'F' and 18 <= age_habitant <= 35) :
    print("L'habitant est imposable.")
else :
    print("L'habitant n'est pas imposable.")