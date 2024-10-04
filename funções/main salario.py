"""Calcular imposto de uma determinada lista de funcionarios"""

from imposto import calcular_imposto

salario_fun = [1200, 1490, 1769, 1222, 1610]

for salario in salario_fun:
    print(calcular_imposto(salario))

input('Pressione ENTER para sair.')