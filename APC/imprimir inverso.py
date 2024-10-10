#Algoritmo que recebe uma palavra e imprime o reverso dessa palavra
palavra = input('Digite uma palavra: ')
# Inicializa uma variável para armazenar a palavra reversa
reversa = ''
#É utilizado o -1, 3 vezes porque: O primeiro -1 ajusta o índice para o último caractere.
#O segundo -1 indica que o loop deve parar antes do índice -1, ou seja, no índice 0.
#O terceiro -1 faz com que o loop percorra a palavra de trás para frente.
for i in range(len(palavra)-1,-1,-1):
    #a cada interação o reversa, recebe um elemento da palavra sendo ela da última a primeira
    reversa += palavra[i]
    print(reversa)

input('Pressione ENTER para sair')