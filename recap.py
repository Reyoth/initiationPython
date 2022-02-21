# variables
var1 = 10 # int
var2 = 4.5 # float
var3 = "bonjour" # string
var4 = True # boolean
var5 = ["bonjour", 5 , 3.5] # list 

print("total est egal a :")
total = var1 + var2
print(total)

# conditions
if var1 > var2:
    print("c'est plus grand")
elif var1 < var2:
    print("c'est plus petit")
else:
    print("c'est egal")

# boucles
while var1 > var2:
    print(var1)
    var1 = var1 - 1

for element in var5:
    print(element)

print("-------------------")
# fonctions
def add(a, b,):
    resultat = a + b
    return resultat
def soust(a, b):
    return a-b

# fonction div, multip, soust




total = soust(var2, var1)
print(total)




