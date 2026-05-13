#ESCALA DE CINZA

#Retirar a cor de uma imagem consiste em calcular a intensidade de luz de cada pixel, baseando-se 
#na forma como o olho humano percebe as cores, realizando uma média ponderada, dando diferentes pesos.
#Fórmula da luminosidade (Brilho): Cinza= 0.299 x R + 0.587 x G + 0.114 x B

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def Escala_Cinza(caminho):
    img = cv.imread(caminho, cv.IMREAD_COLOR_RGB)
    assert img is  not  None , "ERRO: Leitura do Arquivo."
    
    n_linhas, n_colunas, canais = img.shape
    img_cinza = np.zeros_like(img)

    for i in range(n_linhas):
        for j in range(n_colunas):
            img_cinza[i,j]= 0.299 * img[i,j,0] + 0.587 * img[i,j,1] + 0.114 * img[i,j,2] 

    images = [img, img_cinza]
    titles = ['Imagem RGB', 'Imagem Cinza']

    for i in range(2):
        plt.subplot(1,2,i+1),plt.imshow(images[i])
        plt.title(titles[i])

    plt.show()