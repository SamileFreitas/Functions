#Verificar se uma lista é subconjunto de outra lista
lista1 = [1,2,3,4,5,]
lista2 = [7,8,9,4,5,1,2,3]
#primeiro começa com o resultado verdadeiro 
resultado = True
#vai identificar se o número está na lista1, se(if) não estiver na lista2 o reusltado deve ser falso
for numero in lista1:
    if numero not in lista2:
        resultado = False
#definir para impressão o resultado final.
print(resultado)

#perguntando ao usuário quais elementos tem no conjunto/lista.
lista_1 = input('Digite o primeiro conjunto: ')
lista_2 = input('Digite o segundo conjunto: ')
#primeiro começa com o resultado verdadeiro 
resultado = True
#vai identificar se o número está na lista1, se(if) não estiver na lista2 o reusltado deve ser falso
for numero in lista_1:
    if numero not in lista_2:
        resultado = False
#definir para impressão o resultado final.
print(resultado)

input('Precione ENTER para sair')