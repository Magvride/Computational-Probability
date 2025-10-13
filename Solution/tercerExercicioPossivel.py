# Simulación usando LCG
import simulationAlgorithms  # tu módulo para LCG

# Parámetros del LCG
seed1 = 123
seed2 = 456
seed3 = 789
n_sim = 10000  # cantidad de experimentos

# Probabilidades
p_coroa = 0.6
p_cara = 0.4

# Generar números aleatorios usando LCG
lcg1 = simulationAlgorithms.linealCongruentialGenerator(seed1, n_sim)
lcg2 = simulationAlgorithms.linealCongruentialGenerator(seed2, n_sim)
lcg3 = simulationAlgorithms.linealCongruentialGenerator(seed3, n_sim)

# Escalar los números a [0,1]
rand1 = simulationAlgorithms.intervalosLCG(0, 1, lcg1)
rand2 = simulationAlgorithms.intervalosLCG(0, 1, lcg2)
rand3 = simulationAlgorithms.intervalosLCG(0, 1, lcg3)

# Función para convertir números aleatorios en lanzamientos
def lanzar_moneda(rand_list, prob_coroa):
    lanzamientos = []
    for r in rand_list:
        if r < prob_coroa:
            lanzamientos.append(1)  # 1 = coroa
        else:
            lanzamientos.append(0)  # 0 = cara
    return lanzamientos

# Simular lanzamientos
L1 = lanzar_moneda(rand1, p_coroa)
L2 = lanzar_moneda(rand2, p_coroa)
L3 = lanzar_moneda(rand3, p_coroa)

# Evaluar eventos A y B
A = []
B = []
for i in range(n_sim):
    # Evento A: una coroa y una cara en los dos primeros lanzamientos
    if (L1[i] == 1 and L2[i] == 0) or (L1[i] == 0 and L2[i] == 1):
        A.append(1)
    else:
        A.append(0)
    
    # Evento B: dos coroas en los dos últimos lanzamientos
    if L2[i] == 1 and L3[i] == 1:
        B.append(1)
    else:
        B.append(0)

# Calcular probabilidades
P_A = sum(A)/n_sim
P_B = sum(B)/n_sim
P_A_and_B = sum([1 for i in range(n_sim) if A[i]==1 and B[i]==1])/n_sim

# Verificar independencia
independiente = abs(P_A_and_B - P_A*P_B) < 1e-5

# Resultados
print(f"P(A) = {P_A}")
print(f"P(B) = {P_B}")
print(f"P(A ∩ B) = {P_A_and_B}")
print("¿A y B son independientes?", independiente)
