#HISTOGRAMA

#Gráfico que fornece a distribuição de intensidade de uma imagem.
#No eixo x, apresenta os valores de pixel (0-255) e no eixo y, o número de pixels.

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def Histograma(img):

    h = np.zeros(256)
    n_linhas, n_colunas = img.shape

    for i in range(n_linhas):
        for j in range (n_colunas):
            h[img[i, j]] += 1

    return h



