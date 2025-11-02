#A
# Força: entre 10.0 e 20.0; Agilidade: entre 5.0 e 15.0; Inteligência: entre 8.0 e 18.0.
#𝑥𝑘 =(𝑎  × 𝑥𝑘−1 +𝑐) 𝑚𝑜𝑑 𝑀  
#𝑢𝑘 =𝑥𝑘/𝑀 
#com os parâmetros: 𝑎 =39373; 𝑐 =0 ; 𝑀 =2^31 − 1; 𝑥𝑜 =3.

#Supondo que em uma determinada partida do jogo 10 novos personagens precisam ser criados, utilize o algoritmo 
#LCG, com os parâmetros fornecidos, para definir aleatoriamente as características de cada um.


#Lineal congruential Generator 

def lgc(a, x0, c, m):
    x1 = (a*x0+c) % m
    return x1

a = 39373 
c = 0
m = 2^31-1
x0 = 3

fuerza = []
agilidade = []
inteligencia = []

for i in range(10):
    x =lgc(a,x0,c,m)
    fuerza.append(((x/m)*10)+10)
    agilidade.append(((x/m)*10)+5)
    inteligencia.append(((x/m)*10)+8)
    x0 = x

print(fuerza)
print(agilidade)
print(inteligencia)


# Refaça o item anterior utilizando o gerador de números aleatórios padrão do R ou Python. (2,0 pontos)

import random

fuerza1, agilidade1, inteligencia1 = [],[],[]
#O gerador basea-se en Mersenne Twister, gerador de numeros de 0 a 1
random.seed(123)

for i in range(5):
    x = random.random() #Mersenne Twister, gerador de numeros de 0 a 1.
    fuerza1.append((x*10)+10)
    agilidade1.append((x*10)+5)
    inteligencia1.append((x*10)+8)

print(fuerza1,agilidade1, inteligencia1)



direcciones = ['arriba','abajo','izquierda']
pesos = [0.1,0.7,0.2]
print(random.choices(direcciones,pesos, k=8))

