# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:51:06 2020

@author: Anderson
"""

arq= open("Reserva Hotel Atlas.txt", "w")
arq.write('Bem Vindo ao Grand Hotel Atlas\n\n\n')
print('Bem Vindo ao Grand Hotel Atlas')
print()
arq.write('Este programa fará um relatório sobre sua estadia em nosso Hotel - Aproveite ao máximo esta experiência!\n')
print('Este programa fará um relatório sobre sua estadia em nosso Hotel - Aproveite ao máximo esta experiência!')
print()
reserva = input('Gostaria de realizar sua reserva??\nPrecione S para iniciar ou N para cancelar: ')
while(reserva != 'S' and reserva != 's' and reserva != 'N' and reserva != 'n'): 
    print('Tente novamente')
    reserva = input('Gostaria de realizar sua reserva??\nPrecione S para iniciar ou N para cancelar: ')
    
if (reserva =='S') or (reserva =='s'):
        
    #Reserva
    adultos = int(input('Digite o número de adultos que irão se hospedar: '))
    criancas = int(input('Digite o número de crianças que irão se hospedar: '))
    #arq.write('Reserva para ', adultos, 'adultos e para', criancas, 'crianças')
    pessoas = adultos + criancas
    print('\nReserva para', pessoas, 'pessoa(as), sendo ', adultos,'adulto(os) e ', criancas, ' criança(as)' )
    arq.write('\nReserva para {} pessoas'.format(pessoas))
    arq.write('\n{} adulto(os)'.format(adultos))
    arq.write('\n{} criança(as)'.format(criancas))
    print()
    #Entrada Hospedagem
    
    diaEnt=int(input("Digite o dia da entrada: "))
    mesEnt=int(input("Digite o mês da entrada: "))
    anoEnt=int(input("Digite o ano da entrada: "))
    
    #Saída Hospedagem

    diaSai=int(input("Digite o dia da saída: "))
    mesSai=int(input("Digite o mês da saída: "))
    anoSai=int(input("Digite o ano da saída: "))
    diarias = 0

    #Cálculo de diárias apenas para menos de 2 meses de hospedagem

    if(mesEnt==mesSai):
        diarias=diaSai-diaEnt
    else:
         if(mesEnt==1 or mesEnt==3 or mesEnt==5 or mesEnt==7 or mesEnt==8 or mesEnt==10 or mesEnt==12):
             diarias=31-diaEnt
             diarias=diarias+diaSai
         if(mesEnt==2):
             if(anoEnt%4==0):
                 diarias=29-diaEnt
                 diarias=diarias+diaSai
             if(anoEnt%4!=0):
                diarias=28-diaEnt
                diarias=diarias+diaSai
         if(mesEnt==4 or mesEnt==6 or mesEnt==9 or mesEnt==11):
            diarias=30-diaEnt
            diarias=diarias+diaSai
    
    
    arq.write("\n\nO total de diárias é de: {}\n".format(diarias))
    print('\nO total de diárias é de: ', diarias)
    
    #Acomodações

    conta=0
    print('\nSelecione o tipo de acomodação que deseja utilizar')
    print('Selecione uma opção:')
    print('(1) Quarto Simples, com 1 cama de casal - R$ 75,00 diária.')
    print('(2) Quarto Simples, com 2 camas de casal - R$ 140,00 diária.')
    print('(3) Quarto Simples, com 2 camas de solteiro - R$ 80,00 diária.')
    print('(4) Quarto doplo, com 2 cômodos, 1 cama de casal e duas de solteiro - R$ 175,00 diária.')
    print('(5) Quarto Luxo, com 2 cômodos, 2 cama de casal - R$ 200,00 diária.')
    print('(6) Suíte Master - R$ 250,00 diária.')
    print('(0) Encerrar o pedido.')
    
    escolha = int(input('Qual a sua escolha? '))
    print('\nEscolhida a acomodação número', escolha,'.')
    
    while(escolha!=0):
        if (escolha==1):
            conta=conta+75
        if (escolha==2):
            conta=conta+140
        if (escolha==3):
            conta=conta+80
        if (escolha==4):
            conta=conta+175
        if (escolha==5):
            conta=conta+200
        if (escolha==6):
            conta=conta+250
        if (escolha<0 or escolha>6):
            print('\nVerifique o número digitado.')
        print('\nDeseja mais alguma acomodação? Selecione a opção: ')
        print('\n(1) Quarto Simples, com 1 cama de casal - R$ 75,00 diária.')
        print('(2) Quarto Simples, com 2 camas de casal - R$ 140,00 diária.')
        print('(3) Quarto Simples, com 2 camas de solteiro - R$ 80,00 diária.')
        print('(4) Quarto doplo, com 2 cômodos, 1 cama de casal e duas de solteiro - R$ 175,00 diária.')
        print('(5) Quarto Luxo, com 2 cômodos, 2 cama de casal - R$ 200,00 diária.')
        print('(6) Suíte Master - R$ 250,00 diária.')
        print('(0) Encerrar o pedido.')
        escolha = int(input('Digite um número ou ZERO para finalizar: ')) 
        print()
        
    arq.write('\nO valor das acomodações escolhidas é de R$ {},00'.format(conta))
    print('\nO valor das acomodações escolhidas é de R$ ', conta,',00')
        
                
    #Consumo

        
    print('\nIndique o consumo dos produtos oferecidos')
    print('Selecione uma opção:')
    print('\n(1) Garrafa de água, com ou sem gás - R$ 5,00 unidade.')
    print('(2) Lata de refrigerante, 350 ml - R$ 7,00 unidade.')
    print('(3) Garrafa de suco, 200 ml - R$ 6,00 unidade.')
    print('(4) Salgadinho, pacote 60 g - R$ 12,00 unidade.')
    print('(5) Pacote de amendoim, 150 g - R$ 8,00 unidade.')
    print('(6) Mini chocolate em barra, 50 g - R$ 5,00 unidade.')
    print('(0) Encerrar consumo?')
        
    opcao = int(input('Qual a sua escolha? '))
    quantidade = int(input('informe a quantidade: '))
    consumo=0
    while(opcao!=0):
        if (opcao==1):
            consumo=consumo+(5*quantidade)
        if (opcao==2):
            consumo=consumo+(7*quantidade)
        if (opcao==3):
            consumo=consumo+(6*quantidade)
        if (opcao==4):
            consumo=consumo+(12*quantidade)
        if (opcao==5):
            consumo=consumo+(8*quantidade)
        if (opcao==6):
            consumo=consumo+(5*quantidade)
        if (opcao<0 or opcao>6):
            consumo=consumo+0
            print('\nVerifique o número digitado.')
        print('\nDeseja informar mais algum consumo? Selecione a opção:')
        print('(1) Garrafa de água, com ou sem gás - R$ 5,00 unidade.')
        print('(2) Lata de refrigerante, 350 ml - R$ 7,00 unidade.')
        print('(3) Garrafa de suco, 200 ml - R$ 6,00 unidade.')
        print('(4) Salgadinho, pacote 60 g - R$ 12,00 unidade.')
        print('(5) Pacote de amendoim, 150 g - R$ 8,00 unidade.')
        print('(6) Mini chocolate em barra, 50 g - R$ 5,00 unidade.')
        print('(0) Encerrar consumo?')
        opcao = int(input('Digite um número ou ZERO para finalizar: '))
        if(opcao!=0):
            quantidade = 0
            quantidade = int(input('informe a quantidade: '))
        
        
        print('\nO consumo de frigobar foi de: R$', consumo,',00')
        
    conta = conta * diarias
    contaFinal = conta + consumo 
    arq.write('\n\nO consumo de frigobar foi de: R${},00'.format(consumo))
    arq.write('\n\nO valor total a pagar da estadia é de: R${},00'.format(contaFinal))
    print('\nO valor total a pagar da estadia é de: R$ ', contaFinal,',00')
    arq.write('\n\nObrigado pela Preferência!')
    print('\nObrigado pela Preferência!')
    arq.close()
    
#Não realizar checkin
elif (reserva =='N') or (reserva =='n'): 
    arq.write('\nReserva Cancelada\n\nObrigado pela Atenção.')
    print('\nReserva Cancelada\n\nObrigado pela Atenção.')
    
arq.close()

    