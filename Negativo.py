# O que acontece no filtro negativo:
# Este filtro inverte os níveis de intensidade de luz dos pixels de uma imagem
# Visualmente, as áreas claras tornam-se escuras e as áreas escuras tornam-se claras

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def Negativo(img):
    imagem_negativa = np.zeros_like(img)
    dimensao = img.shape
    L = 256 # número de níveis de cinza (0-255 ou 8 bits)

    #escala de cinza apenas
    n_linhas, n_colunas = dimensao
        
    for i in range(n_linhas):
        for j in range(n_colunas):
            r = img[i, j]
            s = L - 1 - r # subtrai o valor do pixel do número de níveis de cinza
            imagem_negativa[i, j] = s #atribui o valor negativo ao pixel correspondente na imagem de saída

    images = [img, imagem_negativa]
    titles = ['Imagem Original', 'Imagem Negativa']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.show()