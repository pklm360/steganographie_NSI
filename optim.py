import PIL.Image

### Entree et verification de l'image et du message ###
fileMessage = 'message'
filePic = 'white'
#fileMessage = input('Adresse du fichier texte (.txt):')


f = open(fileMessage + '.txt')
message = f.read()
f.close()

if len(message) >= 2**15:
    raise Exception("Taille de message trop grande (>32767 symboles)")

#filePic = input("Adresse du l' image initiale (.png):")
img = PIL.Image.open(filePic + '.png')
largeur, hauteur = img.size

if 3*largeur*hauteur <= len(message)*8:
    raise Exception ("Resolution de photo insuffisante pour la taille du texte")

### Encodage en Unicode des lettres ###
print(len(message))
binLength = bin(len(message))
binLength = binLength[:2] + (15-len(binLength))* '0' + binLength[2:]

binLetters = [binLength]
print(binLetters)
for letter in message:
    binCode = bin(ord(letter))
    binCode = binCode[:2] + (10 - len(binCode)) * '0' + binCode[2:] #Ajout de 0s pour normaliser la longeur de chaque element à 10

    binLetters.append((binCode))








### Encodage de la longeur du message ###
i = 0
j = 2
binPixels = []
exit = False
for y in range(hauteur):
    for x in range(largeur):
        if i >= len(message) - 1:
            exit = False
            break
                
        rvb = img.getpixel((x, y))
        for elt in rvb:
  
            if j >= len(binLetters[i]):
                j = 2
                i += 1
            else:
                binPixels.append(bin(elt)[:-1] + binLetters[i][j])
                j += 1



    
    if exit:
        break
print(binPixels[:40])
binTuplesPixels = [(binPixels[i], binPixels[i+1], binPixels[i+2]) for i in range(len(binPixels)-3)]
i = 0
exit = False
for y in range(hauteur):
    for x in range(largeur):
        if i >= len(binTuplesPixels):
            exit = True
            break
        binRvb = binTuplesPixels[i]
        decRvb = []
        for elt in binRvb:
            decRvb.append(int(elt, 2))
        img.putpixel((x, y), tuple(decRvb))
        i += 1
    if exit:
        break

        
        



    










### Sauvegarde de la nouvelle image et affichage de celle-ci ###
img.save('out.png')
img.close()

print(f"Le message a été encodé dans l'image out.png avec succes")
img = PIL.Image.open('out.png')

img.show()
