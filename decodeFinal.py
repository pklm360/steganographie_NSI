import PIL.Image

filePic = 'out'

img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size



binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        binPixels.append(bin(r))
        binPixels.append(bin(v))
        binPixels.append(bin(b))


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





