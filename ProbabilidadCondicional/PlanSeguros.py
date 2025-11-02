import random

planos = ['A','B']
pesos_planos = [0.6,0,4]

planos= random.choices(planos, weights=pesos_planos,k=10)
print(planos)
