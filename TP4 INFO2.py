import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#' Creation d'une fonction d'affichage d'une image
def affimage(img, titre="image", zoom=10):
    cv.namedWindow(titre, cv.WINDOW_NORMAL)
    cv.imshow(titre, img)
    cv.resizeWindow(titre, img.shape[0]*zoom, img.shape[1]*zoom)
    cv.waitKey(0) # attend l’appui sur une touche du clavier
    cv.destroyAllWindows()


#pour creer une matrice de zéro
"""test = np.zeros((4, 5, 1), dtype = "uint8")
print(test)
affimage(test, "Visualisation_Avec_OPENCV")
cv.destroyAllWindows()"""

matrice = np.array([[140, 140, 140, 140, 140, 140, 140, 140, 140],
[110, 30, 31, 32, 33, 34, 35, 36, 110],
[110, 30, 70, 75, 75, 75 , 70, 30, 110],
[110, 30, 70, 225, 225, 225, 70, 30, 110],
[110, 30, 70, 75, 75, 75 , 70, 30, 110],
[110, 30, 31, 32, 33, 34, 35, 36, 110],
[110, 111, 112, 113, 114, 115, 116, 117, 118]], np.uint8) #hauteur, largeur
print(matrice.shape) # affiche les dimensions de la matrice
print(matrice[0,0]) # accède à la valeur du premier pixel

#affichage image
affimage(matrice, "Visualisation_Avec_OPENCV")

# affichage couleur avec zoom
#plt.imshow(matrice, cmap='gray') # affiche la matrice de triplets RVB
#plt.show() # ouvre la fenêtre d’affichage et attend la fin de l’interaction utilisateur

# seuillage
seuil=128
matrice_bin = np.array((matrice>seuil)*255, np.uint8)
print(matrice_bin)
#plt.imshow(matrice_bin, cmap='gray') # affiche la matrice de triplets RVB
#plt.show() # ouvre la fenêtre d’affichage et attend la fin de l’interaction utilisateur

#avec contenu
#affimage(matrice_bin, "matrice binarisee")

hist = cv.calcHist([matrice],[0],None,[255],[0,256])
hist = hist[::, 0]
abscisses = [int(x)*255/(len(hist)-1) for x in range(len(hist))]
plt.bar(abscisses, hist, width=0.5)
plt.title("histogramme matrice initiale")
plt.show()

#numerisation plusieurs niveaux
matrice_num=matrice.copy()

hist2 = cv.calcHist([matrice],[0],None,[20],[0,256])
hist2 = hist[::, 0]
def quatification(matrice,nb_niveau):
#exemple de quantification sur 2 bits (4 niveaux)
# A adapter à votre exemple autant les seuils que les valeurs finales
    for i in matrice:
        matrice_num[matrice < 255] = 200
        matrice_num[matrice < 150] = 100
        matrice_num[matrice<40]=150
