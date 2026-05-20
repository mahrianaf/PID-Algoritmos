# PASSA BAIXA - GAUSSIANO

# O que acontece no filtro Passa Baixa Gaussiano:
# Este filtro suaviza a imagem (efeito de "blur" ou desfoque), reduzindo ruídos e detalhes finos.
# Diferente do filtro de média simples, o filtro Gaussiano dá mais peso ao pixel central
# e pesos progressivamente menores aos pixels vizinhos, criando um desfoque mais natural.
#
# Matematicamente, ele gera uma matriz (kernel) usando a função da distribuição normal (Gaussiana)
# e aplica uma convolução manual: deslizando essa matriz sobre a imagem, multiplicando os valores
# dos pixels vizinhos pelos pesos da matriz e somando tudo para formar a nova intensidade.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def gerar_kernel_gaussiano(tamanho, sigma):
    kernel = np.zeros((tamanho, tamanho))
    meio = tamanho // 2
    
    for x in range(-meio, meio + 1):
        for y in range(-meio, meio + 1):
            # G(x,y) = (1 / 2*pi*sigma^2) * e^(-(x^2+y^2) / 2*sigma^2)
            coeficiente = 1 / (2 * np.pi * sigma**2)
            expoente = -(x**2 + y**2) / (2 * sigma**2)
            
            kernel[x + meio, y + meio] = coeficiente * np.exp(expoente)
            
    return kernel / np.sum(kernel) # Normalização para não estourar o brilho

def PassaBaixaGaussiano(img):
    # Verifica se a imagem é colorida (3 canais) e converte para escala de cinza
    if len(img.shape) == 3:
        img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        img_cinza = img.copy()

    n_linhas, n_colunas = img_cinza.shape
    img_filtro = np.zeros_like(img_cinza, dtype=np.float32)
    
    #O kernel pode ser tanto tamanho 3x3 quanto 5x5 de acordo com a especificação do trabalho, eu escolhi o 3 porque é mais suave
    tamanho_kernel = 3
    sigma = 1.0
    kernel = gerar_kernel_gaussiano(tamanho_kernel, sigma)
    meio = tamanho_kernel // 2

    # Ignoramos as bordas pra simplificar e evitar erros
    for i in range(meio, n_linhas - meio):
        for j in range(meio, n_colunas - meio):
            soma = 0.0
            
            #Percorre ao redor pixel multiplicando pelo kernel
            for x in range(tamanho_kernel):
                for y in range(tamanho_kernel):
                    pixel = img_cinza[i - meio + x, j - meio + y]
                    peso = kernel[x, y]
                    soma += pixel * peso
            
            img_filtro[i, j] = soma

    #Converte os valores de volta para o formato de imagem (int de 8 bits)
    img_filtro = np.uint8(img_filtro)

    images = [img_cinza, img_filtro]
    titles = ['Imagem Original', 'Filtro Gaussiano (Suavizada)']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.show()