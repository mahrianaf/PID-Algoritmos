#PASSA ALTA BASICO

#Objetivo e permitir passar frequências altas (mudanças bruscas) e 
#não permitir frequências baixas (mudanças suaves, áreas uniformes).
#Kernel (máscara) Laplaciano!

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def PassaAlta(img):

    n_linhas, n_colunas = img.shape
    img_filtro = np.zeros_like(img, dtype=np.int32)

    pixel_acima = pixel_esquerda = 0

    for i in range(n_linhas-1):
        for j in range(n_colunas-1):

            pixel_central  = int(img[i,j]) * 4
            pixel_abaixo   = int(img[i+1, j]) * (-1)
            pixel_direita  = int(img[i, j+1]) * (-1)

            if i>0:
                pixel_acima    = int(img[i-1, j]) * (-1)
            if j>0:
                pixel_esquerda = int(img[i, j-1]) * (-1)

            flag = pixel_acima == pixel_abaixo == pixel_esquerda == pixel_direita

            if flag:
                if pixel_central == flag:
                    img_filtro[i, j] = 0
                else:
                    img_filtro[i, j] = 255

    images = [img, img_filtro]
    titles = ['Imagem Original', 'Filtro Passa Alta']

    for i in range(2):
        plt.subplot(1,2,i+1),plt.imshow(images[i])
        plt.title(titles[i])

    plt.show()






