#Transformação Logarítmica
# Este algoritmo expande os valores dos pixels escuros de uma imagem enquanto comprime 
# os valores dos pixels mais claros. Resulta no clareamento geral da imagem,
# revelando detalhes e texturas que estavam escondidos em áreas de sombra.

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def TransformacaoLogaritmica(img):
    # Verifica se a imagem tem 3 canais (colorida) e converte para cinza
    if len(img.shape) == 3:
        img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        img_cinza = img.copy()

    # Converte os pixels pra float para suportar os cálculos matemáticos
    r_float = np.float32(img_cinza)

    # Acha o pixel mais claro da imagem para calcular a constante
    r_max = np.max(r_float)
    c = 255 / np.log(1 + r_max)

    # Aplica a fórmula de transformação logarítmica de forma vetorial
    s_log = c * np.log(1 + r_float)

    # Converte de volta para inteiro de 8 bits de novo
    imagem_log = np.uint8(s_log)

    # Plotagem para comparação
    images = [img_cinza, imagem_log]
    titles = ['Imagem Original', 'Transformação Logarítmica']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.show()