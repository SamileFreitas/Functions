#Calcular IMC de uma lista de pessoas
lista_nome = ['Maria','Fernado','Carlos','Joice']
nome = input('Digite seu nome: ')
#verificar se o nome está na lista.
if nome in lista_nome:
     peso = float(input('Digite seu peso: '))
     altura = float(input('Digite sua altura: '))
     #calcula imc
     imc = peso / altura**2
     print(f'{nome} seu imc é de {imc}.')
else: 
    print('Nome não encontrado na lista')

input('Precione ENTER para sair')