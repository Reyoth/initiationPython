# importer nos librairies
# On nous affiche : entrez un caractere de a->z
# on tape une lettre
# on retrouve la position de la lettre dans alphabet
# on affiche le code morse correspondant a l'index trouve
# le programme nous retourne les symboles correspondants

import liste_morse

print("entrez un caractere de a->z")
lettre= input(">>>")

index = liste_morse.alphabet.index(lettre)
print(liste_morse.morse[index])

