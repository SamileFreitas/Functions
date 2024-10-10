lista = [1, 3, 5, 8, 6, 7, 4]
num1 = 5
num2 = 8
encontrado = False

for i in range(len(lista)-1):
    if lista[i] == num1 and lista[i+1] == num2:
        encontrado = True

if encontrado:
    print('Está em sequência')
else:
    print('Não está em sequência')