#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:32:42 2020

@author: ana claudia costa
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#parâmetros
array_dimensao = np.array([100,200,300,400,500,600,700,800,900,1000])
esparso = 80

array_seed = np.array([1,2,3])
caminho_denso_0_a_9 = './resultados/sem_sono/todos_sem_sono.out'
caminho_sem_sono_0_a_9 = './resultados/sem_sono/todos_sem_sono.out'
caminho_com_sono_0_a_9 = './resultados/com_sono/todos_com_sono.out'


df_denso_menor = pd.read_csv(caminho_denso_0_a_9, delimiter=";")
df_sem_sono_menor = pd.read_csv(caminho_sem_sono_0_a_9, delimiter=";")
df_com_sono_menor = pd.read_csv(caminho_com_sono_0_a_9, delimiter=";")

df_denso = df_denso_menor[df_denso_menor.epsilon == 00]
df_sem_sono = df_sem_sono_menor[df_sem_sono_menor.epsilon == 80]
df_com_sono= df_com_sono_menor[df_com_sono_menor.epsilon == 80]

#tratando os dados densos
df_denso_0 = df_denso[df_denso.epsilon == 00]
media_denso = np.zeros(len(array_dimensao))
for i, dimensao in enumerate (array_dimensao):
    teste = df_denso_0[df_denso_0.alpha == dimensao]
    media_denso[i] = teste["acuracia"].mean()

#tratando os dados sem sono
df_sem_sono_0 = df_sem_sono[df_sem_sono.epsilon != 00]
media_sem_sono = np.zeros(len(array_dimensao))
for i, dimensao in enumerate (array_dimensao):
    teste = df_sem_sono_0[df_sem_sono_0.alpha == dimensao]
    media_sem_sono[i] = teste["acuracia"].mean()

#tratando os dados com sono
df_com_sono_0 = df_com_sono[df_com_sono.epsilon != 00]
media_com_sono = np.zeros(len(array_dimensao))
for i, dimensao in enumerate (array_dimensao):
    teste = df_com_sono_0[df_com_sono_0.alpha == dimensao]
    media_com_sono[i] = teste["acuracia"].mean()

#%% Grafico 
plt.rcParams.update({'font.size': 15})
plt.figure(figsize=(7,5))
for i, j in enumerate (array_seed):
        denso_temp = df_denso_0[df_denso_0.seed == j]
        denso_temp = denso_temp["acuracia"]
        plt.plot( array_dimensao * 0.1 , denso_temp[:len(array_dimensao)]*100, label = "",linewidth=3.0, color = '#58FA82')
        
        df_com_sono_temp = df_com_sono_0[df_com_sono_0.seed == j]
        df_com_sono_temp = df_com_sono_temp["acuracia"]
        plt.plot( array_dimensao * 0.1 , df_com_sono_temp[:len(array_dimensao)]*100, label = "",linewidth=3.0, color = '#87CEFA')
        
        df_sem_sono_temp = df_sem_sono_0[df_sem_sono_0.seed == j]
        df_sem_sono_temp = df_sem_sono_temp["acuracia"]
        plt.plot( array_dimensao* 0.1 , df_sem_sono_temp[:len(array_dimensao)]*100, label = "",linewidth=3.0, color = '#FFA07A')  
                                    

plt.plot( array_dimensao* 0.1 , media_denso[:len(array_dimensao)]*100,label= "Denso", linewidth=3.0, color = 'g')
plt.plot( array_dimensao* 0.1  , media_sem_sono[:len(array_dimensao)]*100, label= "Sem Sono", linewidth=3.0, color = '#FF0000')
plt.plot( array_dimensao* 0.1  , media_com_sono[:len(array_dimensao)]*100, label= "Com Sono", linewidth=3.0, color = '#0000FF')

plt.title("CIFAR - Imagens coloridas")
plt.xlabel('(%)neurônios nas camadas escondidas ')
plt.ylabel('Acurácia (%)')
plt.grid(True)

leg = plt.legend()
plt.legend( numpoints=3, ncol=1, fontsize=13)          
