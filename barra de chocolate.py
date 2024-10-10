#O peso ideal de cada barra é 120g. 
#A indústria define que qualquer variação acima de 5 gramas para mais ou para menos é considerada um defeito, e a barra deve ser descartada.
peso = [120,125,118,122,129,130,121,123,156,120]
limite_max = 120 + 5
limite_min = 120 - 5
avaria = []

for i in range(len(peso)):
    if peso[i] > limite_max or peso[i] < limite_min:
        avaria += [i]

print(avaria, end='')

input('Pressione ENTER para sair')