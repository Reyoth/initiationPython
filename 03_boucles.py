# while : "tant que" la condition est vrai, tu fais...
# for : "pour chaque" element dans une liste, tu fais...

# Exemple 1 --------------------------------------------
fin = 10
debut = 1
# Tant que debut est plus petit que fin, la boucle continue
while debut < fin:
    print("mon compteur = ",debut)
    debut = debut +1 # est equivalent a : debut +=1 

# Exemple 2 --------------------------------------------
texte = "coucou"
# Affiche chaque lettre de notre texte l'une apres l'autre
for lettre in texte :
    print(lettre)

# Exemple 3 --------------------------------------------

texte = "Bonjour"
nbVoyelles = 0
nbConsonnes = 0
# Pour chaque lettre dans texte,
# si la lettre est dans "aeiouy", il compte 1 voyelle en plus
# sinon, il compte une consonne en plus
for lettre in texte :
    if lettre in "aeiouy" :
        nbVoyelles +=1
    else :
        nbConsonnes +=1

print("j'ai", nbConsonnes, "consonnes dans", texte)