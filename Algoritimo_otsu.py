

import histograma as hs
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def otsu(img):
    h = hs.Histograma(img)
    
    n_linhas, n_colunas = img.shape
    total_pixels = n_linhas * n_colunas
    
    p = h / total_pixels
    
    melhor_limiar = 0
    maior_variancia = 0.0
    
    for t in range(256):
        w0 = np.sum(p[:t+1])
        w1 = np.sum(p[t+1:])
        
        if w0 == 0 or w1 == 0:
            continue
            
        u0 = np.sum(np.arange(t+1) * p[:t+1]) / w0
        u1 = np.sum(np.arange(t+1, 256) * p[t+1:]) / w1
        
        variancia_entre = w0 * w1 * ((u0 - u1) ** 2)
        
        if variancia_entre > maior_variancia:
            maior_variancia = variancia_entre
            melhor_limiar = t

  
    img_binarizada = np.zeros_like(img)
    
    for i in range(n_linhas):
        for j in range(n_colunas):
            if img[i, j] >= melhor_limiar:
                img_binarizada[i, j] = 255

    images = [img, img_binarizada]
    titles = ['Original (Cinza)', f'Otsu (Limiar: {melhor_limiar})']

    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.show()