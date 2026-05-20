import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def normalizar_min_max(imagem_float):
    #garante que os pixels fiquem entre 0 e 255 (ou 8 bits)
    t_min = np.min(imagem_float)
    t_max = np.max(imagem_float)
    
    if t_max - t_min == 0:
        return np.uint8(imagem_float)
        
    r = ((imagem_float - t_min) / (t_max - t_min)) * 255
    return np.uint8(r)

def prepara_imagem(img1, img2):
    # Extrai os índices do shape e força a conversão para o inteiro nativo do Python
    altura, largura = img1.shape [:2]                    
    # print(f"Redimensionando imagem 2 para: {img1.shape}")

    #Redimensiona a imagem 2 pra encaixar na imagem 1
    img2_resized = cv.resize(img2, (largura, altura))

    #a gente transforme em float32 pra evitar underflow ou overflow
    f = img1.astype(np.float32)
    h = img2_resized.astype(np.float32)
    return f, h, img2_resized

def exibir_resultados(img1, img2, resultado,operacao):
    #printA as 3 imagens lado a lado 
    images = [img1, img2, resultado]
    titles = ['Imagem 1', 'Imagem 2',operacao]

    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

#eu fiz tudo separado pra caso o usuário queira uma operação só
#a pessoa pode!

def Adicao(img1, img2):
    f, h, img2_resized = prepara_imagem(img1, img2)
    resultado = f + h
    resultado_final = normalizar_min_max(resultado)
    exibir_resultados(img1, img2_resized, resultado_final, 'Resultado: Adição')

def Subtracao(img1, img2):
    f, h, img2_resized = prepara_imagem(img1, img2)
    resultado = f - h
    resultado_final = normalizar_min_max(resultado)
    exibir_resultados(img1, img2_resized, resultado_final, 'Resultado: Subtração')

def Multiplicacao(img1, img2):
    f, h, img2_resized = prepara_imagem(img1, img2)
    resultado = f * h
    resultado_final = normalizar_min_max(resultado)
    exibir_resultados(img1, img2_resized, resultado_final, 'Resultado: Multiplicação')

def Divisao(img1, img2):
    f, h, img2_resized = prepara_imagem(img1, img2)
    # Somamos 1e-5 no divisor para evitar o erro matemático de divisão por zero
    resultado = f / (h + 1e-5)
    resultado_final = normalizar_min_max(resultado)
    exibir_resultados(img1, img2_resized, resultado_final, 'Resultado: Divisão')