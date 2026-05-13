#THRESHOLD

#A partir de um limiar e definido à qual classe (0 ou 255) o pixel pertence.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def Threshold(img):

    ret = np.zeros_like(img)
    dimensao = img.shape

    if len(dimensao) == 2:
        n_linhas, n_colunas = dimensao

        for i in range(n_linhas):
            for j in range (n_colunas):
                if img[i, j] >= 127:
                    ret[i, j] = 255

    elif len(dimensao) == 3:
        n_linhas, n_colunas, n_canais = dimensao

        for k in range(n_canais):
            for i in range(n_linhas):
                for j in range (n_colunas):
                    if img[i, j, k] >= 127:
                        ret[i, j, k] = 255
    
    plotagem(ret)

def plotagem(ret):
    plt.imshow(ret,'gray')
    plt.title("Threshold")
    plt.show()


