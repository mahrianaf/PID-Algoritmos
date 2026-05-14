#PASSA BAIXA BASICO - MEDIA

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def PassaBaixa(img):
    
    n_linhas, n_colunas = img.shape
    pixel_acima = pixel_acima_dir =pixel_esquerda = pixel_abaixo_esq = pixel_acima_esq = 0
    img_filtro = np.copy(img)

    for i in range(n_linhas-1):
        for j in range(n_colunas-1):

            pixel_central  = img[i,j] 
            pixel_abaixo   = img[i+1, j] 
            pixel_direita  = img[i, j+1] 
            pixel_abaixo_dir = img[i+1, j+1]

            if i>0:
                pixel_acima = img[i-1, j]
                pixel_acima_dir = img[i-1, j+1]
            
            if j>0:
                pixel_esquerda = img[i, j-1]
                pixel_abaixo_esq = img[i+1,j-1]
                pixel_acima_esq = img[i-1, j-1]
            
            soma = int(pixel_central) + int(pixel_abaixo) + int(pixel_direita) 
            + int(pixel_abaixo_dir) + int(pixel_acima) + int(pixel_acima_dir) 
            + int(pixel_esquerda) + int(pixel_abaixo_esq) + int(pixel_acima_esq)

            nova_intensidade = soma/9
            img_filtro[i,j] = nova_intensidade

    images = [img, img_filtro]
    titles = ['Imagem Original', 'Filtro Passa Baixa']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])

    plt.show()


