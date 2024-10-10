idade = int(input('Digite a idade do funcionário: '))
tempo_trabalhado = int(input('Digite quantos anos de trabalho tem: '))

if idade >= 65 and tempo_trabalhado >= 30:
    print(f'Funcionário pode ser aposentado, pois tem {idade} anos e {tempo_trabalhado}anos trabalhado na empresa')

elif idade >=60 and tempo_trabalhado >= 25:
    print(f'Funcionário pode ser aposentado, pois tem {idade} anos e {tempo_trabalhado}anos trabalhado na empresa')

else:
    print('O funcionário não cumpri com os requisitos para aposentadoria.')

input('Precione ENTER para sair')