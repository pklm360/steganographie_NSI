import PIL.Image

filePic = 'out'

img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size




binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        rvb = img.getpixel((x, y))
        for i in range(3):
            binPixels.append(bin(rvb[i]))


length = ''
for i in range(15):
    length += binPixels[i][-1]

length = int(length, 2)

binLetters = []
letter = ''

for i in range(15, 15+length*8):

    if len(letter) == 8:
        binLetters.append(chr(int(letter, 2)))
        letter = ""


    letter += binPixels[i][-1]


print("".join(binLetters))





