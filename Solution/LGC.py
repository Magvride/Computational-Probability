print("Algoritmo LGC Linear Congruential Generator")

###### Definición de parametros ##########
x0 = 1 #Semente
a = 6 #Multiplicador
c= 0 #Incremento
m=11  #Maior inteiro representavel na maquina


######## Definición de función ##########

def LGC(x0,a,c,m): 
    seed = x0
    x1 = (a*seed+c) % m
    return x1

#######################################

c = 11 #Definir la cantidad de iteraciones que quiero (cantidad de números aleatorios para generar)
sequencia = [] #Crear matriz que albergue los números
sequencia.append(x0) # Colocar la iteración 0

for i in range(c):
    xn = LGC(x0,a,c,m)
    sequencia.append(xn)
    x0 = xn


print(sequencia)



