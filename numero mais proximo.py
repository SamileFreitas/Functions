#Faça um programa que recebe um conjunto de inteiros e um valor n e indica qual o valor mais próximo de n no conjunto
conj = [10,15,24,19,5,7,8]
num = 14
prox = conj[0]

for valor in conj:
    if num == valor:
        prox = valor
    #se o numero for menor converter em positivo.
    if num < prox:
        dif_prox = -(num - prox)
    else:
        dif_prox = num - prox
    #    #se o valor recebido for menor converter em positivo.
    if num < valor:
        dif_valor = -(num - valor)
    else:
        dif_valor = num - valor
    #comparar se o for atual é mais proximo que a variavel prox
    if dif_valor < dif_prox:
        prox = valor
print(prox)
 
input('Pressione ENTER para sair')