# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:12:09 2020

@author: Anderson
"""
#Leitura das dezenas premiadas
print('\nDigite os numeros sorteados da Megasena:')
d1 = int(input('Digite a primeira dezena:'))
d2 = int(input('Digite a segunda dezena:'))
d3 = int(input('Digite a terceira dezena:'))
d4 = int(input('Digite a quarta dezena:'))
d5 = int(input('Digite a quinta dezena:'))
d6 = int(input('Digite a sexta dezena:'))
  
#Leitura das apostas de 20 apostadores
for num_apostadores in range(1,7):
        acertos=0
        print('\n\nDigite as dezenas do apostador:\n')
        n1 = int(input('Digite a primeira dezena:'))
        n2 = int(input('Digite a segunda dezena:'))
        n3 = int(input('Digite a terceira dezena:'))
        n4 = int(input('Digite a quarta dezena:'))
        n5 = int(input('Digite a quinta dezena:'))
        n6 = int(input('Digite a sexta dezena:'))
        # compare as dezenas apostadas com as sorteadas
        # solução incompleta
        if (n1==d1 or n1==d2 or n1==d3 or n1==d4 or n1==d5 or n1==d6):
            acertos=acertos+1
        if (n2==d1 or n2==d2 or n2==d3 or n2==d4 or n2==d5 or n2==d6):
            acertos=acertos+1
        if (n3==d1 or n3==d2 or n3==d3 or n3==d4 or n3==d5 or n3==d6):
            acertos=acertos+1
        if (n4==d1 or n4==d2 or n4==d3 or n4==d4 or n4==d5 or n4==d6):
            acertos=acertos+1
        if (n5==d1 or n5==d2  or n5==d3 or n5==d4 or n5==d5 or n5==d6):
            acertos=acertos+1
        if (n6==d1 or n6==d2 or n6==d3 or n6==d4 or n6==d5 or n6==d6):
            acertos=acertos+1
        #Resultados por apostador
        print('\n\nTotal de acertos do apostador:\n')
        if (acertos <= 1):
            print('Não foi desta vez... 0 ou 1 acerto.\n')
        if (acertos == 2):
            print('Já foi bem, mas não o suficiente... 2 acertos.\n')
        if (acertos == 3):
            print('Opa, que susto, quase lá... 3 acertos.\n')
        if (acertos == 4):
            print('Já ganhou, mas não muito... 4 acertos.\n')
        if (acertos == 5):
            print('Passou raspando pra ficar milionário... 5 acertos.\n')
        if (acertos == 6):
            print('\o/  Parabéns, você está rico... 6 acertos.\n')
print('final da execução.')    