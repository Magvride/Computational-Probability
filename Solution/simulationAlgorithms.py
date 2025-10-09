print("Algoritmo LGC Linear Congruential Generator")

def linealCongruentialGenerator( semente, cantidadDeNumeros):

    ###### Definición de parametros ##########
    x0 = semente #Semente
    a = 39373 #Multiplicador
    c= 0  #Incremento
    m= 2147483647 #Maior inteiro representavel na maquina
    nsamples = cantidadDeNumeros

    sequencia = [] #Crear matriz que albergue los números
    sequencia.append(x0) # Colocar la iteración 0
    ######## Definición de función ##########

    def LGC(x0,a,c,m): 
        seed = x0
        x1 = (a*seed+c) % m
        return x1
    
    for i in range(nsamples):
        xn = LGC(x0,a,c,m)
        sequencia.append(xn)
        x0 = xn

    return sequencia

def LinealCongruentialGeneratorUnique(x0,a,c,m): 
    seed = x0
    x1 = (a*seed+c) % m  
    return x1

def intervalosLCG(a,b,dados):

    for i in range(len(dados)):
        dados[i] = dados[i]/2147483647
        dados[i]= (dados[i]*(b-a))+a
        
    return dados