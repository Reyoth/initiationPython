liste1 = ["a","b","c"]
#position   0   1   2
liste2 = ["ananas","banane", "citron"]
#position   0          1        2

# print(liste1[0])
# index = liste1.index("c")
# print("position de la lettre = ", index)

print("quelle lettre voulez vous ? a->c")
lettre = input(">>>") #on enregistre la lettre taper au clavier

index = liste1.index(lettre) #on recherche la position de la lettre dans la 1ere liste
print(liste2[index]) #on affiche le mots qui correspond a la position