# importer nos librairies
# On nous affiche : entrez un caractere de a->z
# on tape une lettre
# on retrouve la position de la lettre dans alphabet
# on affiche le code morse correspondant a l'index trouve
# le programme nous retourne les symboles correspondants

import liste_morse

# encoder un mots en morse
print("entrez un un mots")
mots= input(">>>")
code=""
# bonjour
for lettre in mots:
    code = code + liste_morse.encode(lettre)
    code = code + " "
print(code)

#------------------------
# on decode un code morse en mots
print("entrez un code morse")
code = input(">>>")
mots=""
#"--- -. ---"
#[---, -., ---]
# On decoupe notre code en liste de code separe par un espace
liste_code = str.split(code," ")
#on affiche le resultat de la decoupe
print(liste_code)
# pour chaque element de la liste_code, on recupere la lettre correspondante et on
# la stoque dans la viriable mots
for element in liste_code:
    mots = mots + liste_morse.decode(element)

print(mots)


