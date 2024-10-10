#Para cada valor entre inicio e fim faça:
# ação
#range = limite do 'for' sendo de um em um, sem o passo de interação apenas com o inicio e fim ou apenas com o fim
# for 'variavel' in range(limite de repetição 'inicio, fim) ou # for 'variavel' in range(limite de repetição, fim)

#Utilizar o for em que a repetição seja com um determinado número de repetição.
#utilizando em três ponto, sendo eles de: range(inicio, fim e "passo de interação")
##range = limite do 'for'
# for 'variavel' in range(limite de repetição 'inicio, fim e passo de interação)

soma = 0
for i in range(0,10):
    #para realizar a 
    soma = soma + i
#quando quer receber apenas o final da soma dos números da lista.
print(soma)

soma = 0
for i in range(0,10):
    #para imprimir os números da lista em par.
    if i % 2 == 0:
        soma = soma + i
print(soma)

soma = 0
for i in range(0,10):
    #para imprimir os números da lista em ímpar.
    if i % 2 == 1:
        soma = soma + i
print(soma)

input('Precione ENTER para sair')