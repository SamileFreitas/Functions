valor = int(input('Digite o valor que deseja sacar: '))

print('')

if valor >= 100:
    quant_cem = valor // 100
    print(f'100 = {quant_cem}')

valor = valor % 100

if valor >= 50:
    quant_cinquenta = valor // 50
    print(f'50 = {quant_cinquenta}')

valor = valor % 50

if valor >= 10:
    quant_dez = valor // 10
    print(f'10 = {quant_dez}')

valor = valor % 10

if valor >= 5:
    quant_cinco = valor // 5
    print(f'5 = {quant_cinco}')

valor = valor % 5

print(f'1 = {valor}')

input('Precione ENTER para sair')