def calcular_cedulas(valor):
    cedulas = [100, 50, 10, 5, 1]
    resultado = {}

    for cedula in cedulas:
        quantidade, valor = divmod(valor, cedula)
        if quantidade > 0:
             resultado[cedula] = quantidade

    return resultado

valor_saque = int(input('Digite o valor que deseja sacar: '))
cedulas = calcular_cedulas(valor_saque)

print(f'Para o valor de R$:{valor_saque}, você precisa das seguintes cédulas: ')
for cedula, quantidade in cedulas.items():
    print(f'Cédulas de R${cedula}:{quantidade}')

input('Precione ENTER para sair')