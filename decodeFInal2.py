import PIL.Image

### Entree et verification de l'image ###
filePic = 'out'


img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size




length = ''
for x in range(5):
    rvb = img.getpixel((x, 0))
    for i in range(3):
        length += bin(rvb[i])[-1]

length = int(length, 2)
print(length)
nbPixelsRestants = length
binPixels = []
for y in range(hauteur):
    if nbPixelsRestants < largeur:
        largeurParcours = nbPixelsRestants
    else:
        largeurParcours = largeur
    for x in range(largeurParcours):
        rvb = img.getpixel((x, y))
        for i in range(3):
            binPixels.append(bin(rvb[i]))
    nbPixelsRestants -= largeur
print(len(binPixels))

### Decodage des lettres ###
binLetters = []
letter = ''


for i in range(length*3): #On commence le decodage à l'indice 15
    if len(letter) == 8:

        binLetters.append(chr(int(letter, 2)))
        letter = ""


    letter += binPixels[i][-1]

print(len(binLetters))
#print("".join(binLetters))





