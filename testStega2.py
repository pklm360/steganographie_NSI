import PIL.Image

fileMessage = 'message.txt'
f = open(fileMessage)
message = f.read()
f.close()

# if len(message) > 31:
#     raise Exception("Taille de message trop grande (>31 symboles)")


binLetters = [bin(len(message))]
for letter in message:
    binCode = bin(ord(letter))


    binLetters.append((binCode)) #Enlever le 0b ici ou apres ? l.33

img = PIL.Image.open('white.png')
largeur, hauteur = img.size




binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        binPixels.append(str(bin(r)))
        binPixels.append(str(bin(v)))
        binPixels.append(str(bin(b)))
print(binPixels[:30])

newBinPixels = []
posInBinPixels = 0
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
        r, v, b = int(mergedBinPixels[j], 2), int(mergedBinPixels[j+1], 2), int(mergedBinPixels[j+2], 2)
        j += 3
        img.putpixel((x, y), (r, v, b))





img.save('out.png')
img.close()

img = PIL.Image.open('out.png')
img.show()
