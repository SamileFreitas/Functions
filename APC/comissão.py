nome = input('Qual o nome do corretor? ')
valor_vendido = float(input('Qual o valor vendido por ele? '))
comissao = 0

# Quando é utilizado muitos números para calcular uma porcentagem, posso utilizar o if, elif e else
# para fazer o calculo de tal porcentagem. Sendo assim, não preciso inserir valores muitas vezes ou o mesmo calculo.

if valor_vendido <30000.00:
    comissao = 7
elif valor_vendido >=30000.00 <50000.00:
    comissao = 9.5
else:
    comissao = 12

comissao_receber = (valor_vendido*comissao)/100
print(f'A comissão do vendedor é: {comissao_receber}')

input('Precione ENTER para sair')