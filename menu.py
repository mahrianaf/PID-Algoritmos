import threshold as th
import histograma as hs
import equalizacao as eq
import escala_de_cinza as ec
import passa_baixa_media as pb
import passa_alta_basico as pa
import sobel as sb
import cv2 as cv

#Imagem 1: ./assets/lobo.webp
#Imagem 2: ./assets/jurassic-park.jpg

while True:
    print(" _________________________ ")
    print("|       ALGORITMOS        |")
    print("|                         |")
    print("| [1] Carregar Imagem     |")
    print("| [2] Threshold           |")
    print("| [3] Histograma          |")
    print("| [4] Equalização         |")
    print("| [5] Escala de Cinza     |")
    print("| [6] Passa Baixa - Média |")
    print("| [7] Passa Alta - Básico |")
    print("| [8] Passa Alta - Sobel  |")
    print("| [0] Encerrar            |")
    print("|_________________________|\n")

    opcao = input("Opção: ")

    if opcao == "1":
        caminho = input()
        img = cv.imread(caminho, cv.IMREAD_GRAYSCALE)
        assert img is  not  None , "ERRO: Leitura do Arquivo."

    elif opcao == "2":
        th.Threshold(img)
        
    elif opcao == "3":
        hs.Histograma(img)

    elif opcao == "4":
        eq.Equalizacao(img)

    elif opcao == "5":
        ec.Escala_Cinza(caminho)

    elif opcao == "6":
        pb.PassaBaixa(img)
        
    elif opcao == "7":
        pa.PassaAlta(img)

    elif opcao == "8":
        sb.Sobel(img)
        
    elif opcao == "0":
        print("Encerrado!")
        break
    else:
        print("Opção Inválida!")
