import simulationAlgorithms

c = 10
a = 1
b = 6
maiorInteiro = 2147483647
numeros = []

for i in range(c) :

    dado1= simulationAlgorithms.linealCongruentialGenerator(3,39373,0,2147483647,1)
    dado1 = dado1/maiorInteiro
    dado1 = (dado1 * (b-1))+a
    numeros.append(dado1)

print(numeros)


