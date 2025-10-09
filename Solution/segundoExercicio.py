import simulationAlgorithms
import matplotlib.pyplot as plt
import random 

#c = 10
#a = 1
#b = 6
maiorInteiro = 2147483647
#numeros = []

#dados1 = simulationAlgorithms.linealCongruentialGenerator(3,39373,0,2147483647,10000)
#dados2 = simulationAlgorithms.linealCongruentialGenerator(3,39373,0,2147483647,10000)
#sumaDados = []
#print(dados1)

#for i  in range(len(dados1)):
    #dados1[i]= dados1[i]/maiorInteiro
    #dados1[i] = int((dados1[i]*6)+1)
    #dados2[i]= dados2[i]/maiorInteiro
    #dados2[i] = int((dados2[i]*6)+1)
    #multiplico por 6 porque eu preciso pegar 6 numeros inteiros, se eu fizer só por 5, teria só numero 5 
    # o qual nao é possivel porque preciso  ter diferentes 6 opciones.
    #suma= dados1[i]+dados2[i]
    #sumaDados.append(suma)

numeroSimulaciones = 0
sumaDados = []
c=0
semente1 = 3
semente2 = 2
dados1 = []
dados2 = []

while(c ==0 ):
    
    semente1 = simulationAlgorithms.LinealCongruentialGeneratorUnique(semente1,39373,0,2147483647)
    semente2 = simulationAlgorithms.LinealCongruentialGeneratorUnique(semente2,39373,0,2147483647)
    dado1 = semente1/maiorInteiro
    dado2 = semente2/maiorInteiro
    dado1 = int((dado1*6)+1)
    dados1.append(dado1)
    dado2 = int((dado2*6)+1)
    dados2.append(dado2)
    suma = dado1 + dado2
    print(f"dado1: {dado1}, dado2: {dado2}, suma: {suma}")
    print(suma)
    

    if suma in sumaDados:
        print("Repitió")
    else: 
        sumaDados.append(suma)

    if len(sumaDados)==11:
        print("Acabou")
        c =1
        print(f"La cantidad de simulaciones necesarias fueron {numeroSimulaciones}")

    numeroSimulaciones= numeroSimulaciones+1
    
    print(sumaDados)


#Cria o histograma
plt.hist(dados1, bins=10, color="green", edgecolor="black")

# Adiciona título e rótulos
plt.title("Histograma dados1")
plt.xlabel("Valores")
plt.ylabel("Frequência")

# Mostra o gráfico
plt.show()

#Cria o histograma
plt.hist(dados2, bins=10, color="green", edgecolor="black")

# Adiciona título e rótulos
plt.title("Histograma dados2")
plt.xlabel("Valores")
plt.ylabel("Frequência")

# Mostra o gráfico
plt.show()



#Conclusión : según este algoritmo son necesarias 40 simulaciones con las siguientes sementes 
# a = 123456
# b = 78910

