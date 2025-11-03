import random 
import pandas as pd

nsamples = 1000000
primerRamificacion = random.choices(['DA','DB','DC'], weights=[0.4,0.3,0.3], k=nsamples)


segundaRamificacion = []

for pr in primerRamificacion:

    if pr  == 'DA':
        sr = random.choices(['BC','CB'], weights=[0.65,0.35])[0]
        segundaRamificacion.append(sr)

    elif pr =='DB':
        sr = random.choices(['AC','CA'], weights=[0.45,0.55])[0]
        segundaRamificacion.append(sr)

    else:
        sr = random.choices(['AB','BA'], weights=[0.6,0.4])[0]
        segundaRamificacion.append(sr)


terceraRamificacion = []

for pr, sr in zip(primerRamificacion, segundaRamificacion):

    if pr == 'DA' and sr =='BC':
        
        tr = random.choices(['AB','BA'], weights=[0.6,0.4])[0]
        terceraRamificacion.append(tr)

    elif pr=='DA' and sr=='CB':
        tr = random.choices(['CA','AC'], weights=[0.55,0.45])[0]
        terceraRamificacion.append(tr)

    elif pr=='DB' and sr=='AC':
        tr = random.choices(['AB','BA'], weights=[0.6,0.4])[0]
        terceraRamificacion.append(tr)

    elif pr=='DB' and sr=='CA':
        tr = random.choices(['CB','BC'], weights=[0.35,0.65])[0]
        terceraRamificacion.append(tr)

    elif pr=='DC' and sr=='AB':
        tr = random.choices(['CA','AC'], weights=[0.55,0.45])[0]
        terceraRamificacion.append(tr)

    elif pr=='DC' and sr=='BA':
        tr = random.choices(['CB','BC'], weights=[0.35,0.65])[0]
        terceraRamificacion.append(tr)


df = pd.DataFrame({'Descanso': primerRamificacion, 'PrimerDuelo':segundaRamificacion, 'SegundoDuelo':terceraRamificacion})

print(df)

ganharA = []
ganharB = []
ganharC = []

for g in terceraRamificacion:

    if g=='AB' or g=='AC':

        ganharA.append(g)
    
    elif g=='BA' or g=='BC':

        ganharB.append(g)
    
    elif g=='CB' or g=='CA':

        ganharC.append(g)

#------------------------ Punto A ---------------------------------------------------

print('Prbabilidade de ganhar A:', len(ganharA)/nsamples)
print('Prbabilidade de ganhar B:', len(ganharB)/nsamples)
print('Prbabilidade de ganhar C:', len(ganharC)/nsamples)

#------------------------ Punto B ---------------------------------------------------

df['OrdemEliminacao'] = df.apply(lambda x: (
    x['PrimerDuelo'][1],  # perdedor do primeiro duelo
    x['SegundoDuelo'][1]  # perdedor do segundo duelo
), axis=1)


prob_ordem = df['OrdemEliminacao'].value_counts(normalize=True)
print(prob_ordem)

#------------------------ Punto C ---------------------------------------------------

# Filtrar apenas simulações em que A venceu o primeiro duelo
# ['PrimerDuelo'].str[0]  .. pega o primeiro carater do str
# filtar cuando primer duelo tiene de primera la letra A
df_A_venceu1 = df[df['PrimerDuelo'].str[0] == 'A']

# Contar quantas dessas A venceu o segundo duelo (ou seja, venceu a etapa)
n_vitoria_A = (df_A_venceu1['SegundoDuelo'].str[0] == 'A').sum()

# Total de simulações em que A venceu o primeiro duelo
total_A_primeiro = len(df_A_venceu1)

# Probabilidade condicional
prob_A = n_vitoria_A / total_A_primeiro
print('Probabilidade de A vencer a etapa dado que venceu o primeiro duelo:', prob_A)


##------------------------ Punto D ---------------------------------------------------

df_B_eliminado = df[df['PrimerDuelo'].str[1]=='B']
df_C_venceu = (df_B_eliminado['SegundoDuelo'].str[0]=='C').sum()

probabilidade = df_C_venceu/len(df_B_eliminado)
print('Probabilidade de C vencer a etapa dado que B foi eliminado no primeiro duelo:', probabilidade)

##------------------------ Punto E ---------------------------------------------------

df_b_descansa_c_vence =df[(df['Descanso']=='B') & (df['PrimerDuelo'].str[0] =='C')]
probabilidade = df_C_venceu/len(df_b_descansa_c_vence)
print('Probabilidade de C vencer a etapa dado que B descansou e C ganhou no primeiro duelo:', probabilidade)

##Isso faz sentido no campeonato: se B descansa, o primeiro duelo é A vs C, então C não pode ganhar contra 
# A com frequência suficiente para aparecer nos seus dados, dependendo das probabilidades.