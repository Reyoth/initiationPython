alphabet=["a",
"b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q",
"r","s","t","u","v","w","x","y","z"," "]

morse=[".-",
"-...",
"-.-.",
"-..",
".",
"..-.",
"--.",
"....",
"..",
".---",
"-.-",
".-..",
"--",
"-.",
"---",
".--.",
"--.-",
".-.",
"...",
"-",
"..-",
"...-",
".--",
"-..-",
"-.--",
"--..",
" "]

#encode lettre > code morse
def encode(lettre):
    # on cherche l'index de la lettre dans la liste alphabet
    index = alphabet.index(lettre)
    #on recherche le code morse correspondant a l'index
    code_morse= morse[index]
    #on renvoit le code morse trouve
    return code_morse

#decode code morse > lettre
def decode(code):
    index = morse.index(code)
    lettre = alphabet[index]
    return lettre



#print(alphabet.__len__())
#print(morse.__len__())