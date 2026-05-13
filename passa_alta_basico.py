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
    px_min = px_max = 0

    for i in range(n_linhas-1):
        for j in range(n_colunas-1):

            pixel_central  = int(img[i,j]) * 4
            pixel_abaixo   = int(img[i+1, j]) * (-1)
            pixel_direita  = int(img[i, j+1]) * (-1)

            if i>0:
                pixel_acima    = int(img[i-1, j]) * (-1)
            if j>0:
                pixel_esquerda = int(img[i, j-1]) * (-1)

            img_filtro[i, j] = abs(pixel_central + pixel_abaixo + pixel_direita + pixel_acima + pixel_esquerda)

            if px_max < img_filtro[i, j]:
                px_max = img_filtro[i, j]

            if px_min > img_filtro[i, j]:
                px_min = img_filtro[i, j]

    img_final = normalizacao(px_max, px_min, img_filtro)

    images = [img, img_final]
    titles = ['Imagem Original', 'Filtro Passa Alta']

    for i in range(2):
        plt.subplot(1,2,i+1),plt.imshow(images[i])
        plt.title(titles[i])

    plt.show()

def normalizacao(px_max, px_min, img):
    n_linhas, n_colunas = img.shape

    for i in range( n_linhas):
        for j in range( n_colunas):
            img[i,j] = ((img[i,j] - px_min)/(px_max - px_min) * 255)

    return img






