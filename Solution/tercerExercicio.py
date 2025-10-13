import simulationAlgorithms 
import random
import matplotlib.pyplot as plt

Probabilidadecoroa= 3/5
Probabilidadecara= 2/5


dado1 = simulationAlgorithms.linealCongruentialGenerator(123, 100000)
dado2 = simulationAlgorithms.linealCongruentialGenerator(456, 100000)
dado3 = simulationAlgorithms.linealCongruentialGenerator(789, 100000)

dadosSequencia= simulationAlgorithms.intervalosLCG(0,1,dado1)
dadosSequencia2= simulationAlgorithms.intervalosLCG(0,1,dado2)
dadosSequencia3= simulationAlgorithms.intervalosLCG(0,1,dado3)


def caraouCoroa(dadosSequencia, probabilidade):
    cc = []
    for i in range(len(dadosSequencia)):
        if(dadosSequencia[i]<(1-probabilidade)):
            cc.append(1)#coroa

        else:
            cc.append(0)#cara

    #print(f"A probabilidade de ter coroa foi de {sum(cc)/100000}")
    #print(f"A probabilidade de ter cara foi de {(1000-sum(cc))/100000}")
    return cc



dado1 =caraouCoroa(dadosSequencia,Probabilidadecara)
dado2= caraouCoroa(dadosSequencia2,Probabilidadecara)
dado3 = caraouCoroa(dadosSequencia3,Probabilidadecara)

#𝐴 = “obter uma coroa e uma cara nos dois primeiros lançamentos, em qualquer ordem”, e 
#𝐵 = “obter duas coroas nos dois últimos lançamentos”

def probabilidadesEventos(arreglo1,arreglo2,arreglo3):
    probabilidadesEventos =[]
    for i in range(len(arreglo1)):

        if(arreglo1[i] == 1 and arreglo2[i]== 0):
            probabilidadesEventos.append("A")
            #print(f"Lanzamiento uno fue cara, Lanzamiento dos fue coroa, Lanzamiento tres fue {arreglo3[i]}")
        elif(arreglo1[i]==0 and arreglo2[i]==1):
            probabilidadesEventos.append("A")
            #print(f" Lanzamiento uno fue coroa, Lanzamiento dos fue cara, Lanzamiento tres {arreglo3[i]}")
        elif(arreglo2[i]==1 and arreglo3[i]==1):
             #print(f" Lanzamiento dos fue coroa, Lanzamiento tres fue cora, Lanzamiento uno fue {arreglo1[i]}")
             probabilidadesEventos.append("B")
        else:
            probabilidadesEventos.append("C")
            #print(f"Lanzamiento uno fue {arreglo1[i]}, Lanzamiento uno fue {arreglo2[i]}, Lanzamiento uno fue {arreglo3[i]}")
        
    return probabilidadesEventos


#print(probabilidadesEventos(dado1,dado2,dado3))
probabilidades =probabilidadesEventos(dado1,dado2,dado3)

plt.hist(probabilidades ,bins = 10, color="green", edgecolor ="black")
plt.show()

print(f"La probabilidad del evento A ocurrir es {(probabilidades.count("A")/100000)*100}% ")
print(f"La probabilidad del evento B ocurrir es {(probabilidades.count("B")/100000)*100}%")
print(f"La probabilidad del evento C ocurrir es {(probabilidades.count("C")/100000)*100}%")






