#Buscar um elemento em uma lista de inteiros
#criar a lista
lista = [1,2,3,4,5,6,7,8,9,10]
#perguntar sobre o elemnte de busca
elemento = int(input('Digite qual elemento busca na lista: '))
#utilizar if e in(index) para realizar a busca pelo o elemento dentro da lista
if elemento in lista:
   print('O numero está na lista')
else:
   print('O numero não está na lista')

input('Precione ENTER para sair')