#calcular média de uma lista de inteiros

#listar os valores de números inteiros a ser utilizado
lista = [1,2,3,4,5,6,7,8,9,10]
#necessário para fazer a soma de todos os valores inteiro
soma = 0
for i in lista:
    #para a soma de todos os números inteiros, necessário para fazer a média.
    soma += i
    #para realizar a média 
    media = soma / len(lista)
print(media)

input('Precione ENTER para sair')