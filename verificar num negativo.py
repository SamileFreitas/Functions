#Faça um programa que recebe um conjunto de inteiros e verifica se existe algum número negativo no conjunto
num = [2,5,8,-9,4,-1,3,7,-4,6,3]
cont = 0

for i in range(len(num)):
    if num[i] < 0:
        cont += 1
print(f'O total de número negativos é de {cont}')

input('Pressione ENTER para sair')