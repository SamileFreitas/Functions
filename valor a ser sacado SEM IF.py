valor = int(input('Digite o valor que você deseja sacar: '))

print('')

print(f'100 = {valor // 100}')
valor = valor % 100

print(f'50 = {valor // 50}')
valor = valor % 50

print(f'10 = {valor // 10}')
valor = valor % 10

print(f'5 = {valor // 5}')
valor = valor % 5

print(f'1 = {valor // 1}')

input('Precione ENTER para sair')