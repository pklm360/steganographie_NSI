import PIL.Image

### Entree et verification de l'image ###
filePic = 'out'


img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size



### Recuperation des valeurs RVB de chaque pixels ###
binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        rvb = img.getpixel((x, y))
        for i in range(3):
            binPixels.append(bin(rvb[i]))

### Decodage de la longeur du message ###
length = ''
for i in range(15):
    length += binPixels[i][-1]

length = int(length, 2)

### Decodage des lettres ###
binLetters = []
letter = ''

for i in range(15, 15+length*8): #On commence le decodage à l'indice 15

    if len(letter) == 8:
        binLetters.append(chr(int(letter, 2)))
        letter = ""


    letter += binPixels[i][-1]


print("".join(binLetters))





