#Tendo  como  entrada  a  altura  e  o  sexo  (codificado  da  seguinte  forma: 1:feminino    2: masculino)  de  uma  pessoa,  
# construa  um  programa  que calcule e imprima seu peso ideal, utilizando as seguintes 
#Fórmulas: 
#- para homens: (72.7 * Altura) – 58 
#- para mulheres: (62.1 * Altura) – 44.7 


nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo, utilizando M(masculino) e F(feminino): ')

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é de: {peso_ideal}kg')
if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é de: {peso_ideal}kg')

input('Precione ENTER para sair')