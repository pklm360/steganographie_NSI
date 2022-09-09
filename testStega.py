import PIL.Image

fileMessage = 'loremIpsum.txt'
f = open(fileMessage)
message = f.read()
f.close()

# if len(message) > 31:
#     raise Exception("Taille de message trop grande (>31 symboles)")


binLetters = []
for letter in message:
    binCode = bin(ord(letter))[2:]


    binLetters.append((9-len(binCode))*'0'+ binCode) #Enlever le 0b ici ou apres ? l.33

img = PIL.Image.open('white.png')
largeur, hauteur = img.size




binPixels = [str(bin(len(message)))]
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        binPixels.append(str(bin(r))[2:])
        binPixels.append(str(bin(v))[2:])
        binPixels.append(str(bin(b))[2:])

posInBinPixels = 0
for elt in binLetters:
    for i in range(len(elt)):
        originalVal = binPixels[posInBinPixels]
        binPixels[posInBinPixels] = originalVal[:-1] + elt[i]



        posInBinPixels += 1

j = 0
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = int(binPixels[j], 2), int(binPixels[j+1], 2), int(binPixels[j+2], 2)
        j += 3
        img.putpixel((x, y), (r,v,b))




img.save('out.png')
img.close()

img = PIL.Image.open('out.png')
img.show()