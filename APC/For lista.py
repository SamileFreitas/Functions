#Lista armazenamento de elementos dentro da memoria
#contagem sempre começa em ZERO
# += mesma variavel, então é a soma dentro da propria variavel
#len = tamanho da lista

lista = [1,5,8,7,10]
#lista = [0,1,2,3,4] elementos dentro da caixa de memoria
print(len(lista))
print(lista)
#posição dois
print(lista[2])
#posição zero
print(lista[0])
#posição -1 - sendo ela a última da lista
print(lista[-1])

#soma de todos os números da lista
soma = 0
for i in range(0,5):
    soma = soma + lista[i]
    print(soma)
print('')
#soma final do numero da lista
soma = 0
for i in range(0,5):
    soma = soma + lista[i]
print(soma)
print('')
#soma final com o tamanho de len
soma = 0
for i in range(len(lista)):
    soma = soma + lista[i]
print(soma)
print('')
#imprimir apenas os elementos da lista com suas posições
lista = [1,5,8,7,10,8,-1,5,4]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(f'{i}: {lista[i]}')
print('')
#manipulação de lista para que mostre apenas os numeros
for numero in lista:
    print(numero)
print('')
#manipulação de lista para que mostre apenas os numeros pares
for numero in lista:
    if numero % 2 == 0:
         print(numero)
print('')
#para mostrar a posição e o número (enumerate)
for i,numero in enumerate(lista):
    if numero % 2 == 0:
         print(i,':',numero)

input('Precione ENTER para sair')