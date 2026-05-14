# O que acontece no filtro negativo:
# Este filtro inverte os níveis de intensidade de luz dos pixels de uma imagem
# Visualmente, as áreas claras tornam-se escuras e as áreas escuras tornam-se claras

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def Negativo(img):
    # Verifica se a imagem é colorida e converte para escala de cinza
    if len(img.shape) == 3:
        img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        img_cinza = img.copy()

    n_linhas, n_colunas = img_cinza.shape
    imagem_negativa = np.zeros_like(img_cinza)
    L = 256 # número de níveis de cinza (0-255 ou 8 bits)

    for i in range(n_linhas):
        for j in range(n_colunas):
            r = img_cinza[i, j]
            s = L - 1 - r # subtrai o valor do pixel do número de níveis de cinza
            imagem_negativa[i, j] = s #atribui o valor negativo ao pixel correspondente na imagem de saída

    #Printa
    images = [img_cinza, imagem_negativa]
    titles = ['Original (Cinza)', 'Imagem Negativa']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.show()