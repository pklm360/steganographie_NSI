import PIL.Image

# fileMessage = 'loremIpsum.txt'
# filePic = 'black.png'
fileMessage = input('Adresse du fichier texte (.txt):')


f = open(fileMessage + '.txt')
message = f.read()
f.close()

if len(message) >= 2**15:
    raise Exception("Taille de message trop grande (>31 symboles)")

filePic = input("Adresse du l' image initiale (.png):")
img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size

if 3*largeur*hauteur< len(message):
    raise Exception ("Resolution de photo insuffisante pour la taille du texte")


binLetters = [bin(len(message))]
for letter in message:
    binCode = bin(ord(letter))


    binLetters.append((binCode)) #Enlever le 0b ici ou apres ? l.33





binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        binPixels.append(str(bin(r)))
        binPixels.append(str(bin(v)))
        binPixels.append(str(bin(b)))


newBinPixels = []
binLength = bin(len(message))[2:]
for i in range(15):
    if i < len(binLength):
        newBinPixels.append(binPixels[i][:-1] + binLength[i])
    else:
        newBinPixels.append(binPixels[i])



posInBinPixels = 15

for elt in binLetters:
    for i in range(2, len(elt)):
        originalVal = binPixels[posInBinPixels]
        encryptedVal = originalVal[:-1] + elt[i]
        encryptedVal = encryptedVal[:2] + (11 - len(encryptedVal)) * '0' + encryptedVal[2:]

        newBinPixels.append(encryptedVal)


        posInBinPixels += 1


mergedBinPixels = newBinPixels + binPixels[len(newBinPixels):]
j = 0
for y in range(hauteur):
    for x in range(largeur):
        if j >= len(newBinPixels):
            break
        r, v, b = int(mergedBinPixels[j], 2), int(mergedBinPixels[j+1], 2), int(mergedBinPixels[j+2], 2)
        j += 3
        img.putpixel((x, y), (r, v, b))




fileOut = input('Nom du fichier de sortie (.png):')
img.save(fileOut + '.png')
img.close()

print(f"Le message a été encodé dans l'image {fileOut}.png avec succes")
img = PIL.Image.open('out.png')
img.show()
