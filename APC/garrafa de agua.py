#Cada garrafa deve ter um volume de 500 ml. 
# #Qualquer variação acima de 10 ml para mais ou para menos é considerada um defeito, e a garrafa deve ser descartada.
volume = [495,520,490,505,470,500,495,489,532]
limite_max = 500 + 10
limite_min = 500 - 10
avaria = []

for i in range(len(volume)):
    if volume[i] > limite_max or volume[i] < limite_min:
        avaria += [i]

print(avaria, end='')

input('Pressione ENTER para sair')