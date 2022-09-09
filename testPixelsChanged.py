import PIL.Image


img = PIL.Image.open('white.png')
largeur, hauteur = img.size

binPixels = []
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        # print(bin(r), bin(v), bin(b))
        binPixels.append(str(bin(r)))
        binPixels.append(str(bin(v)))
        binPixels.append(str(bin(b)))

print(binPixels[:25])
# binLetters = ['0b100101010']
# binPixels = ['0b111111110'] * 9
# newBinPixels = []
# posInBinPixels = 0
# for elt in binLetters:
#     for i in range(2, len(elt)):
#         originalVal = binPixels[posInBinPixels]
#         print(originalVal)
#         encryptedVal = originalVal[:-1] + elt[i]
#         print(encryptedVal, elt[i])
#         encryptedVal = encryptedVal[:2] + (11 - len(encryptedVal)) * '0' + encryptedVal[2:]
#
#         print(encryptedVal)
#         newBinPixels.append(encryptedVal)
#
#
#         posInBinPixels += 1