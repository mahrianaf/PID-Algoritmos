from matplotlib import pyplot as plt
import threshold as th
import histograma as hs
import equalizacao as eq
import escala_de_cinza as ec
import passa_baixa_media as pb
import passa_alta_basico as pa
import Negativo as ng
import Transf_logaritimica as tl
import Passa_baixa_g as pbg
import operacao as op
import sobel as sb
import cv2 as cv

#Imagem 1: ./assets/lobo.webp
#Imagem 2: ./assets/jurassic-park.jpg

while True:
    print(" _______________________________")
    print("|       ALGORITMOS              |")
    print("|                               |")
    print("| [ 0] Carregar Imagem          |")
    print("| [ 1] Threshold                |")
    print("| [ 2] Histograma               |")
    print("| [ 3] Equalização              |")
    print("| [ 4] Escala de Cinza          |")
    print("| [ 5] Passa Baixa - Média      |")
    print("| [ 6] Passa Alta - Básico      |")
    print("| [ 7] Passa Alta - Sobel       |")
    print("| [ 8] Transf. Logarítmica      |")
    print("| [ 9] Negativo                 |")
    print("| [10] Passa Baixa - Gaussiano  |")
    print("| [11] Operações Aritméticas    |")
    print("| [ x] Encerrar                 |")
    print("|_______________________________|\n")

    opcao = input("Opção: ")

    if opcao == "0":
        caminho = input("Imagem: ")
        img = cv.imread(caminho, cv.IMREAD_GRAYSCALE)
        assert img is  not  None , "ERRO: Leitura do Arquivo."

    elif opcao == "1":
        th.Threshold(img)
        
    elif opcao == "2":
        h = hs.Histograma(img)
        plt.plot(h)
        plt.show()

    elif opcao == "3":
        eq.Equalizacao(img)

    elif opcao == "4":
        ec.Escala_Cinza(caminho)

    elif opcao == "5":
        pb.PassaBaixa(img)
        
    elif opcao == "6":
        pa.PassaAlta(img)

    elif opcao == "7":
        sb.Sobel(img)
        
    elif opcao == "8":
        tl.TransformacaoLogaritmica(img)

    elif opcao == "9":
        ng.Negativo(img)
    
    elif opcao == "10":
        pbg.PassaBaixaGaussiano(img)

    elif opcao == "11":
        print(" _______________________________")
        print("|     OPERAÇÕES ARITMÉTICAS     |")
        print("|                               |")
        print("| [ 1] Adição                   |")
        print("| [ 2] Subtração                |")
        print("| [ 3] Multiplicação            |")
        print("| [ 4] Divisão                  |")
        print("|_______________________________|\n")

        sub = input("Opção: ")
        if sub == "1":
            caminho2 = input("Segunda Imagem: ")
            img2 = cv.imread(caminho2, cv.IMREAD_GRAYSCALE)
            assert img2 is not None, "ERRO: Leitura do Arquivo."
            op.Adicao(img, img2)

        elif sub == "2":
            caminho2 = input("Segunda Imagem: ")
            img2 = cv.imread(caminho2, cv.IMREAD_GRAYSCALE)
            assert img2 is not None, "ERRO: Leitura do Arquivo."
            op.Subtracao(img, img2)

        elif sub == "3":
            caminho2 = input("Segunda Imagem: ")
            img2 = cv.imread(caminho2, cv.IMREAD_GRAYSCALE)
            assert img2 is not None, "ERRO: Leitura do Arquivo."
            op.Multiplicacao(img, img2)

        elif sub == "4":
            caminho2 = input("Segunda Imagem: ")
            img2 = cv.imread(caminho2, cv.IMREAD_GRAYSCALE)
            assert img2 is not None, "ERRO: Leitura do Arquivo."
            op.Divisao(img, img2)

    elif opcao == "x":
        print("Encerrado!")
        break
    else:
        print("Opção Inválida!")
