agenda = [[],[],[],[],[]]

#definição das listas, perguntando ao usuário
for i in range(5):
    nome = input('Digite nome: ')
    telefone = input('Digite telefone: ')
    encontrado = False
    #verificar se o nome já existe na agenda
    for j in range(len(agenda)):
        if agenda[j] and agenda[j][0] == nome:
            agenda[j][1] = telefone #atualiza o número de telefone se o nome já existir
            encontrado = True
    #adicionar o contato se o número não foi encontrado após loop
    for l in range(len(agenda)):
        if encontrado == False:
            if len(agenda[l]) == 0: #encontrar o primeiro espaço da agenda
                agenda[l] = [nome, telefone]
                encontrado = True #marcar que o contato foi adicionado
print(agenda)

input('Pressione ENTER para sair')