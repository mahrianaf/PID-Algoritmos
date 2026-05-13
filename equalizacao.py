#EQUALIZACAO DE HISTOGRAMA

#Ajusta o contraste de uma imagem, distribuindo os valores dos pixels de forma mais uniforme.

from matplotlib import pyplot as plt
from histograma import Histograma
import numpy as np  
import cv2 as cv

def Equalizacao(img):

    n_linhas, n_colunas = img.shape
    total = n_linhas * n_colunas

    n = np.zeros(256) 
    s = np.zeros(256)

    #1. Histograma h(rk) = nk
    h = Histograma(img)

    for i in range(256):

        #2. Normalizado p(rk) = nk/MN 
        n[i]= (h[i]/ total) 

        #3. Transformacao s = p * 255
        n[i] = n[i] * 255

        #4. Soma Acumulativa
        s[i] = s[i-1] + n[i] if i > 0 else n[i]
    
    equalized = np.zeros_like(img)

    for i in range(n_linhas):
        for j in range(n_colunas):
            equalized[i,j]= s[img[i,j]]
    
    plt.plot(h, label='Original')
    plt.plot(Histograma(equalized), label='Equalizado')
    plt.legend()
    plt.show()






