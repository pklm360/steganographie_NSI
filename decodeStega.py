import PIL.Image

# filePic = input("Adresse du l' image initiale (.png):")
filePic = "out"
img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size


def addElt(couleur, elt):
    elt += couleur[-1]
    if len(elt) > 9:
        binLetters.append(elt)
        elt = ""

binLetters = []
elt = ""
for y in range(hauteur):
    for x in range(largeur):
        r,v,b = img.getpixel((x, y))

        elt += bin(r)[-1]
        if len(elt) == 9:
            binLetters.append(elt)
            elt = ""

        elt += bin(v)[-1]
        if len(elt) == 9:
            binLetters.append(elt)
            elt = ""

        elt += bin(b)[-1]
        if len(elt) == 9:
            binLetters.append(elt)
            elt = ""

textLst = []
for elt in binLetters:
    textLst.append(chr(int('0b' + elt, 2)))












