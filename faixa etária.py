idade = int(input('Qual é sua idade? '))


if idade <= 0:
    print('Idade inválida')
elif idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')

input('Precione ENTER para sair')