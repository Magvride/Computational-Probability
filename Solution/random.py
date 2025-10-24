import random 

direcciones = ['arriba','abajo','izquierda']
pesos = [0.1,0.7,0.2]
print(random.choices(direcciones,pesos, k=1))
