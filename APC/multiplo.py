def verificar_multiplos(num1, num2):
    if num2 == 0:
        return False # não se pode dividir zero
    return num1 % num2 == 0

num1 = int(input('Digite um número: '))
multiplo_de = int(input('Digite um número para verificar se é múltiplo: '))

if verificar_multiplos(num1, multiplo_de):
    print(f'{num1} é múltiplo de {multiplo_de}')
else:
    print(f'{num1} não é múltiplo de {multiplo_de}')

input('Precione ENTER para sair')