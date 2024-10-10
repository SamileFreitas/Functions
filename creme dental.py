#A máquina está sendo utilizada para filtrar creme dental. Um item correto tem peso de 90g. 
# Para a indústria, qualquer variação acima de 2 gramas para mais ou para menos, é considerada
#uma avaria no produto, e este não pode seguir para venda.
peso = [90,90,91,90,93,90,89,90,87,90,85,91,90,90,86]
limite_max = 90 + 2
limite_min = 90 - 2
avaria = []

for i in range(len(peso)):
    if peso[i] > limite_max or peso[i] < limite_min:
        avaria += [i]

print(avaria, end=',')

input('Pressione ENTER para sair')