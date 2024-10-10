#4 avaliações
nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))
nota4 = float(input('Digite a nota4: '))
#a cada 2 avaliação formam uma AB
AB1 = (nota1+nota2)/2
AB2 = (nota3+nota4)/2
#se a média1 de AB1 e AB2 >= 7 aprovado
media1 = (AB1 + AB2)/2

if media1 >= 7:
    print(f'Aprovado!')
#senão reavaliação substitui a menor AB se ela é amior que a AB
else:
    reavaliação = float(input('Digita a nota de reavaliação: '))

    if AB1 <= AB2 and reavaliação > AB1:
        AB1 = reavaliação
    elif AB1 > AB2 and reavaliação > AB2:
        AB2 = reavaliação
    #média2 = reavaliação + a outra AB
    media2 = (AB1+AB2)/2
    #se média2 >= 7 aprovado
    if media2 >= 7:
        print(f'Aprovado!')
    #senão, e a média2 < 5 reprovado
    elif media2 < 5:
        print('Reprovado!')
    #senão faz a prova final
    else:
        final = float(input('Digite a nota final: '))
    #nota final = média2 * 0.6 + final * 0.4
    nota_final = media2 * 0.6 + final * 0.4
    #se a nota final >= 5.5 então aprovado
    if nota_final >= 5.5:
        print('Aprovado!')
    #senão reprovado.
    else:
        print('Reprovado!')

input('Precione ENTER para sair')