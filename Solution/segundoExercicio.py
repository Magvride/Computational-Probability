import simulationAlgorithms
import matplotlib.pyplot as plt

c = 10
a = 1
b = 6
maiorInteiro = 2147483647
numeros = []

dados1 = simulationAlgorithms.linealCongruentialGenerator(3,39373,0,2147483647,100000)
print(dados1)
for i  in range(len(dados1)):
    dados1[i]= dados1[i]/maiorInteiro
    dados1[i] = int((dados1[i]*6)+1)
    #multiplico por 6 porque eu preciso pegar 6 numeros inteiros, se eu fizer só por 5, teria só numero 5 
    # o qual nao é possivel porque preciso  ter diferentes 6 opciones.

print(dados1)

# Cria o histograma
plt.hist(dados1, bins=10, color="green", edgecolor="black")

# Adiciona título e rótulos
plt.title("Histograma de dado 1")
plt.xlabel("Valores")
plt.ylabel("Frequência")

# Mostra o gráfico
plt.show()
plt.savefig("Histograma de frecuencias dos valores do dado 1.png")



