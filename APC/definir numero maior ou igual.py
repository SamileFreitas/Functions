# Escreva um programa para ler 2 valores e escrever o maior deles ou se são iguais.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
maximo = max(valor1, valor2)

if valor1 == valor2:
 print('Os valores digitados são iguais.')

elif valor1 < valor2:
 print(f'Os valores digitados não são iguais, pois o valor maior é: {maximo}')

else:
 print(f'Os valores digitados não são iguais, pois o maior é: {maximo}')

input('Precione ENTER para sair')