import simulationAlgorithms
import matplotlib.pyplot as plt


nsamples = 10000
semente = 3 # por que a semente inicializa num número 3?
multiplicador = 39373
maiorInteiro = 2147483647
incremento = 0

cara_coroa= simulationAlgorithms.linealCongruentialGenerator(semente,multiplicador,incremento,maiorInteiro,nsamples)
for i in range(len(cara_coroa)):
    cara_coroa[i] = cara_coroa[i]/maiorInteiro

print(cara_coroa)

# Cria o histograma
plt.hist(cara_coroa, bins=10, color="green", edgecolor="black")

# Adiciona título e rótulos
plt.title("Histograma de Cara ou Coroa")
plt.xlabel("Valores")
plt.ylabel("Frequência")

# Mostra o gráfico
plt.show()
plt.savefig("Histograma de frecuencias dos numeros gerados.png")


print(len(cara_coroa)) #1001


#a uniformidade é apenas a base, mas o que queremos 
#é transformar esses números em um evento binário
def probabilidadCaraCoroa(sequencia,probabilidade):
    cc = []
    for i in range(len(sequencia)):
        if(sequencia[i]>(1.0-probabilidade)):
            cc.append(0)#cara
        else:
            cc.append(1)#coroas
    return cc


probabilidade = probabilidadCaraCoroa(cara_coroa, 0.5)
print(sum(probabilidade))
#A suma foi de 4985 coroas y 5016 caras 

print(f"A probabilidade de ter coroa foi de {sum(probabilidade)/10001}")
print(f"A probabilidade de ter cara foi de {(10001-sum(probabilidade))/10001}")


