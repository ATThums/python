# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:33:27 2020

@author: Anderson
"""

print('\n\n\nAIUrb - Análise de Índices Urbanísticos')

#Trabalho de Lógica computacional

#ENTRADA DE DADOS

#Letras maiúsculas para parâmetros e minúsculas para variáveis.

A = 0 
IA = 0
TO = 0
TP = 0
H = 0
AFE = 0
AL = 0
Pv = 0
h = 0
pve = 0


mf = float(input('\nInforme a Medida Frontal do terreno (m): '))
ml = float(input('\nInforme a Medida Lateral do terreno (m): '))
ia = float(input('Informe o Índice de Aproveitamento do terreno, conforme o Plano Diretor do município: '))
to = float(input('Informe a Taxa de Ocupação do terreno (%), conforme o Plano Diretor do município: '))
tp = float(input('Informe a Taxa de Permeabilidade do terreno (%), conforme o Plano Diretor do município: '))
lv = float(input('\nInforme a Largura da Via, referente a fachada principal do terreno (m): '))
print('\n\n*Se você já possue a altura que deseja construir, digite ZERO para o Afastamento Frontal Efetivo, para que seja fornecido posteriormente')
afe = float(input('Informe o Afastamento Frontal Efetivo, referente a fachada principal do terreno: '))
if (afe == 0):
    h = float(input('\nInforme a altura a qual pretende construir: '))
pd = float(input('\nInforme a altura do Pé Direito que pretende construir: '))

#PROCESSAMENTOS

A = mf * ml
IA = ia * A
TO = (to * A)/100
TP = (tp * A)/100


if (afe != 0):
    H = 1.5 * (lv + afe)
    Pv = H//pd
    pve = round(Pv)
else:
    AFE = H/1.5 - lv
    Pv = h//pd
    pve = round(Pv)
    H = h
AL = 2 + (H - lv)/5


#SAÍDA DE DADOS

print(f'\nA Área do terreno é de {A} metros quadrados')
print(f'O Índice de Aproveitamento do terreno é de {IA} metros quadrados')
print(f'A Taxa de Ocupação do terreno é de {TO} metros quadrados')
print(f'A Taxa de Permeabilidade do terreno é de {TP} metros quadrados')
if (afe != 0):
    print(f'A Altura máxima permitida para o AFE escolhido é de {H} metros')
if (afe == 0):
    print(f'O Afastamento frontal Efetivo é de {AFE} metros')
print(f'O Afastamento Lateral é de {AL} metros')
print(f'O Número de pavimentos estimados sobre o afastamento é de {pve} pavimentos')

Aliv = A - TO - TP 

import matplotlib.pyplot as plt
labels = ['Área Livre', 'Taxa de Ocupação', 'Taxa de Permeabilidade']
titulos = [Aliv, TO, TP]
cores = ['lightblue', 'green', 'yellow', 'red']
explode = (0.1, 0, 0)  # somente explode primeiro pedaço
total = sum(titulos)
plt.title('Área Total do Terreno')
plt.pie(titulos, explode=explode, labels=labels, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 
100), shadow=True, startangle=90)
# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
plt.axis('equal') 
plt.show()


#grafico de BARRAS
import matplotlib.pyplot as plt
y = [IA,A]
N = len(y)
x = range(N)
width = 0.5
plt.bar(x, y, width, color="red")
plt.xlabel('')
plt.ylabel('((m) Metros)')
plt.title('Índice de Aproveitamento')
plt.show()
