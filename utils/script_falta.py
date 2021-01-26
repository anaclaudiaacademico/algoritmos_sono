#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:20:20 2021

@author: ana claudia
"""
import os
import numpy as np

caminho_denso_0_a_9 = '~/resultados/sem_sono/'
caminhos = [os.path.join(caminho_denso_0_a_9, nome) for nome in os.listdir(caminho_denso_0_a_9)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
csv = [arq for arq in arquivos if arq.lower().endswith(".csv")]

base = 0
numfiles = 4

fff = []
for ii in np.arange(numfiles):
    fff.append(open('input/npad_input_file_%d.txt' % (base+ii),'w'))

pythoncode = "caminho_comando_python"
datapos = "caminho_onde_resultado_sera_escrito"
scriptfile = "arquivo_python_que_sera_executado"


nsteps = 1000
v_input_dim =  np.array([0.1000,0.2000,0.3000,0.4000,0.5000,0.6000,0.7000,0.8000,0.9000,1.0])
v_sparseness = np.array([0.00])
v_seed = np.arange(1,8)

erros = 0
acertos = 0
for jj,input_dim in enumerate(v_input_dim):
    for ii,sparseness in enumerate(v_sparseness):
        for ss,seed in enumerate(v_seed):
    


            fffile = "%s %s %s  %f %f %d %d" % (pythoncode,
                                                                scriptfile,
                                                                datapos,
                                                                input_dim,
                                                                sparseness,
                                                                nsteps,
                                                                seed)  
            
            if ("/resultados/sem_sono/log_cifar_sparse_sem_sono_decimal_alpha%.5d_epsilon%.5d_seed%.5d.csv"
                %(input_dim*1000,sparseness*100, seed) ) in csv:
                    print("existe")
                    acertos = acertos +1
            else:
                print("não existe")
                lllog = " > ./log/out_ana_decimal_%.5d_%.5d_%.5d_%.1d.txt" % (input_dim*1000, sparseness*100, nsteps, seed)
                fff[ss%numfiles].write(fffile+lllog+'\n')
                print(lllog)
                print("~/resultados/sem_sono/log_cifar_sparse_sem_sono_decimal_alpha%.5d_epsilon%.5d_seed%.5d.csv"
                %(input_dim*1000,sparseness*100, seed) )

                erros = erros +1  

for ii in np.arange(numfiles):
    fff[ii].close()
