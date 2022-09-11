import PIL.Image

### Entree et verification de l'image et du message ###
fileMessage = 'message'
filePic = 'james_bond'
#fileMessage = input('Adresse du fichier texte (.txt):')


f = open(fileMessage + '.txt')
message = f.read()
f.close()

if len(message) >= 2**15:
    raise Exception("Taille de message trop grande (>31 symboles)")

#filePic = input("Adresse du l' image initiale (.png):")
img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size

if 3*largeur*hauteur< len(message):
    raise Exception ("Resolution de photo insuffisante pour la taille du texte")

### Encodage en Unicode des lettres ###
binLetters = []
for letter in message:
    binCode = bin(ord(letter))
    binCode = binCode[:2] + (10 - len(binCode)) * '0' + binCode[2:] #Ajout de 0s pour normaliser la longeur de chaque element à 10

    binLetters.append((binCode))



### Recuperation des valeurs RVB de chaque pixels ###
binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        binPixels.append(str(bin(r)))
        binPixels.append(str(bin(v)))
        binPixels.append(str(bin(b)))


### Encodage de la longeur du message ###
newBinPixels = []
binLength = bin(len(message))[2:]
binLength = (15-len(binLength))* '0' + binLength #Ajout de 0s pour que binLength soit de taille 0

for i in range(15):
    newBinPixels.append(binPixels[i][:-1] + binLength[i]) #Encodage de la taille du message dans les codes RVB des 5 premiers pixels





### Encodage des lettres ###
posInBinPixels = 15 #On commence l'encodage à l'indice 15 (6eme pixel)

for elt in binLetters:
    for i in range(2, len(elt)):
        originalVal = binPixels[posInBinPixels]
        encodedVal = originalVal[:-1] + elt[i] #Le bit de pois faible (dernier element de la chaine) est remplace par les valeurs de chaque element de binLetters (elt)
        newBinPixels.append(encodedVal)


        posInBinPixels += 1

###Insertion des nouvelles valeurs des pixels ###
mergedBinPixels = newBinPixels + binPixels[len(newBinPixels):]
j = 0
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = int(mergedBinPixels[j], 2), int(mergedBinPixels[j+1], 2), int(mergedBinPixels[j+2], 2)
        j += 3
        img.putpixel((x, y), (r, v, b))









### Sauvegarde de la nouvelle image et affichage de celle-ci ###
img.save('out.png')
img.close()

print(f"Le message a été encodé dans l'image out.png avec succes")
img = PIL.Image.open('out.png')

# lst = []
# for y in range(hauteur):
#     for x in range(largeur):
#         r, v, b = img.getpixel((x, y))
#         #print(bin(r), bin(v), bin(b))
#         lst.append(str(bin(r)))
#         lst.append(str(bin(v)))
#         lst.append(str(bin(b)))
#
# for i in range(len(newBinPixels)):
#     print(lst[i], newBinPixels[i])

img.show()