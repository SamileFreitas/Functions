#Algoritmo que recebe uma palavra e conta quantas vogais há na palavra
palavra = input('Digite uma palavra: ')
vogais = 'a','e','i','o','u'
cont = 0

for i in palavra:
    if i in vogais:
        cont += 1
print(f'A quantidade de vogais na palavra {palavra} é de {cont}')

input('Pressione ENTER para sair')