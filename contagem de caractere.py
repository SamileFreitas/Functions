palavra = input('Digite uma palavra:  ')
caractere = input('Digite uma caractere: ')
cont = 0
# Percorre cada caractere da palavra
for letra in palavra:
    # Verifica se o caractere é igual ao caractere buscado
    if letra == caractere:
        cont += 1
print(f'O caractere {caractere} aparece {cont} vezes na palavra {palavra}')

input('Pressione ENTER para sair')