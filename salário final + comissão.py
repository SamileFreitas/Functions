def calcular_salario_final(num_de_carros, valor_total_vendas, salario_fixo, valor_do_carro):
    
    comissao_por_carro_vendido = num_de_carros * valor_do_carro

    comissao_por_venda = 0.05 * valor_total_vendas
    salario_final = salario_fixo + comissao_por_carro_vendido + comissao_por_venda
    return salario_final

salario_fixo = float(input('Qual o valor do sálario fixo do vendedor? '))
num_de_carros = float(input('Quantos carros foram vendidos? '))
valor_do_carro = float(input('Qual o valor unitário do carro? '))
valor_total_vendas = float(input('Qual o valor total das vendas? '))

salario_final = calcular_salario_final(num_de_carros, valor_total_vendas, salario_fixo, valor_do_carro)
print(f'O salário final do vendedor é: R$:{salario_final:.2f}')

input('Precione ENTER para sair')