#PASSA ALTA - SOBEL

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import math 

def Sobel(img):

    n_linhas, n_colunas = img.shape
    img_filtro = np.zeros_like(img, dtype=np.int32)

    pixel_acima = pixel_acima_dir =pixel_esquerda = pixel_abaixo_esq = pixel_acima_esq = 0
    soma = soma_Gx = soma_Gy = 0

    Gx= np.zeros(9, dtype=np.int32)
    Gy= np.zeros(9, dtype=np.int32)

    for i in range( n_linhas-1):
        for j in range( n_colunas-1):

            soma_Gx = soma_Gy = 0

            pixel_central  = img[i,j] 
            Gx[0] = pixel_central * 0
            Gy[0] = pixel_central * 0

            pixel_abaixo   = img[i+1, j] 
            Gx[1] = pixel_abaixo * 0
            Gy[1] = pixel_abaixo.astype(np.int32) * 2

            pixel_direita  = img[i, j+1] 
            Gx[2] = pixel_direita.astype(np.int32) * 2
            Gy[2] = pixel_direita * 0

            pixel_abaixo_dir = img[i+1, j+1]
            Gx[3] = pixel_abaixo_dir * 1
            Gy[3] = pixel_abaixo_dir * 1

            if i>0:
                pixel_acima = img[i-1, j]
                Gx[4] = pixel_acima * 0
                Gy[4] = int(pixel_acima) * (-2)

                pixel_acima_dir = img[i-1, j+1]
                Gx[5] = pixel_acima_dir * 1
                Gy[5] = int(pixel_acima_dir) * (-1)
            
            if j>0:
                pixel_esquerda = img[i, j-1]
                Gx[6] = int(pixel_esquerda) * (-2)
                Gy[6] = pixel_esquerda * 0

                pixel_abaixo_esq = img[i+1,j-1]
                Gx[7] = int(pixel_abaixo_esq) * (-1)
                Gy[7] = pixel_abaixo_esq * 1

                pixel_acima_esq = img[i-1, j-1]
                Gx[8] = int(pixel_acima_esq) * (-1)
                Gy[8] = int(pixel_acima_esq) * (-1)
            
            for k in range(9):
                soma_Gx += Gx[k]
                soma_Gy += Gy[k]
            
            img_filtro[i, j] = math.sqrt(soma_Gx**2 + soma_Gy**2)

    # Normalização
    maior_valor = img_filtro.max()
    if maior_valor > 0:
        img_final = (img_filtro / maior_valor * 255).astype(np.uint8)
    else:
        img_final = img_filtro.astype(np.uint8)

    images = [img, img_final]
    titles = ['Imagem Original', 'Filtro Sobel']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])

    plt.show()

# Observacao: Gx e Gy foram definidos como int (aceitam numeros positivos e negativos)
# porem, durante a multiplicacao de numeros negativos com as variaveis pixels, estava dando um erro
# "Python integer -2 out of bounds for uint8" mesmo Gx e Gy estando corrigidos, mas o problema era 
# que as variaveis pixels eram do tipo unint8, por isso foram convertidas para int para poderem 
# ser multiplicadas. Alem disso, tambem foi adicionado essa mascara nas multiplicacoes dos pixels
# com 2, pois estava aparecendo o erro: "RuntimeWarning: overflow encountered in scalar multiply
# Gx[2] = pixel_direita * 2".