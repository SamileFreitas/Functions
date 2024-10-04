""" Escreva um programa que possui uma função que recebe uma lista e diz qual a soma máxima entre dois elementos da lista"""

def calc_valor(lista):
    #primeiro preciso saber o tamanho e utilizar dois numeros
    if len(lista) < 2:
        return None
    # Inicializa os dois maiores números com os dois primeiros elementos
    if lista[0] > lista[1]:
        maior1 = lista[0]
        maior2 = lista[1]
    else:
        maior1 = lista[1]
        maior2 = lista[0]

    for num in lista[2:]:
        if num > maior1:
            maior2 = maior1 #atualiza o segundo numero
            maior1 = num #atualiza o primeiro numero
        elif num > maior2:
            maior2 = num #atualiza o segundo maior
    #retorne a soma dos dois numeros
    return maior1 + maior2
