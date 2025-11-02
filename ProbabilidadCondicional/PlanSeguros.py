import random
import pandas as pd


#Nivel 1 Ramificación - Plan A e Plan B

planos = ['A','B']
pesos_planos = [0.6,0.4]
nsamples = 1000000


planos= random.choices(planos, weights=pesos_planos,k=nsamples)

#------------------------------------------------------------------------

#Nivel 2 Ramificação - Maior ou menor de 30 

#crea una matriz
edades = []

for plano in planos:
##Necesita crear la condición porque las probabilidades van a variar 
# Dependiendo el plano 

    if plano == 'A':
        #Caso la ramificación sea A, se dan las probabilidades de los 
        # Grupos de la faxia etaria determinada
        edad  = random.choices(['<=30','>30'], weights=[0.3,0.7])[0]
        edades.append(edad)

    else:
        edad  = random.choices(['<=30','>30'], weights=[0.5,0.5])[0]
        edades.append(edad)

#------------------------------------------------------------------------

#Nivel 3 de Ramificación 

#Crear arreglo que contiene los sinistros 
sinistros = []

for plano,edad in zip(planos,edades):

    ## En este punto se deben crear las cuatros diferentes probabilidades
    # que están presentes en el nivel 3 del diagrama

    #Primera posibilidad : P(G1|A)

    if plano == 'A' and edad == '<=30':

        sinistro = random.choices(['s','-s'], weights=[0.03,0.97])[0]
        sinistros.append(sinistro)
      
    #Segunda posibilidad : P(G2|A)

    elif plano == 'A' and edad == '>30':

        sinistro = random.choices(['s','-s'], weights=[0.015,0.985])[0]
        sinistros.append(sinistro)

    #Tercer Posibilidad: P(G1|B)

    elif plano == 'B' and edad == '<=30':
        sinistro= random.choices(['s','-s'],weights = [0.06, 0.94])[0]
        sinistros.append(sinistro)

    else:

    #Cuarta posibiliad : P(G2|B)

        sinistro = random.choices(['s','-s'], weights=[0.04,0.96])[0]
        sinistros.append(sinistro)

#------------------------------------------------------------------------

#Crear un dataframe que contiene los diferentes usuarios 
dataframe = pd.DataFrame({'Plano': planos,'Edad-Grupo': edades, 'Sinistro': sinistros})

Probabilidad_B_S = dataframe[dataframe['Sinistro']=='s']['Plano'].value_counts(normalize=True)
print(Probabilidad_B_S)

Probabilidad_g1_s = dataframe[dataframe['Sinistro']=='s']['Edad-Grupo'].value_counts(normalize=True)
print(Probabilidad_g1_s)

Probabilidad_B_SeG1 = dataframe[(dataframe['Sinistro']=='s') & (dataframe['Edad-Grupo']=='<=30')]['Plano'].value_counts(normalize=True)
print(Probabilidad_B_SeG1)

#-------------------------------- Respostas -------------------------------------------

#Plano
# B    0.630542  (Resposta A)
# A    0.369458


# Edad-Grupo
# <=30    0.559103 (Resposta B)
# >30     0.440897

# Plano
# B    0.683238 (Resposta C)
# A    0.316762
