hora_trabalhada = int(input('Digite a quantidade de horas trabalhado na semana: '))
valor_hora = float(input('Digite o valor da hora de trabalho: '))
hora_regular = 40
acrescimo = 0.5

if hora_trabalhada <= hora_regular:
    print(f'Foi trabalhado {hora_trabalhada}h, sendo cada hora no valor de R$ {valor_hora} reais. Então o salário final é no valor de: R$ {hora_trabalhada * valor_hora}' )
else: 
    salario = hora_regular * valor_hora
    print(f'Foi trabalhado {hora_trabalhada}h, sendo cada hora no valor de R$ {valor_hora} reais. Então o salário final é no valor de: R$ {salario + hora_trabalhada * acrescimo}')

input('Precione ENTER para sair')