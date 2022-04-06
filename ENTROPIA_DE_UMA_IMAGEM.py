# bibliotecas necessárias
from matplotlib import pyplot as plt #biblioteca de gráficos
import numpy as np # biblioteca de calculos
import cv2 # importa biblioteca que processa imagens


informacao=0 # inicia variável informacao com 0
entropia=0  # inicia variável entropia com 0
image = cv2.imread("frog.pgm") #carrega imagem
hist = cv2.calcHist([image], [0], None, [256], [0, 256])#calcula histograma
probabilidades = hist/ hist.sum()#distribuiçao percentual dos tons de 0 a 255
tam=len(probabilidades)#tamanho do vetor probabilidades no caso 256

for i in range (tam):   #for com 256 ciclos
   
   if(probabilidades[i]!=0):   # se p(x) diferente de zero 
      informacao += (-hist[i]*np.log2(probabilidades[i])) # informacao da imagem 
      entropia += (-probabilidades[i]*np.log2(probabilidades[i])) #entropia da imagem
      

print("Informaçao da imagem:",informacao,"bits")  #imprime o valor da informacao
print("Entropia da imagem:",entropia,"bits/simbolo")#imprime o valor da entropia
print(hist.sum())
print(hist[0])
print(hist[255])
print(image)
#plota imagem
plt.figure()
plt.axis("off")
plt.imshow(image)
# plota o histograma
plt.figure()
plt.title(" Histograma da escala de cinza")
plt.xlabel("amostras")
plt.ylabel("# por Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


