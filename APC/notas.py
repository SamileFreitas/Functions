notas_alunos = [['Ana',10,8.5],['Calos',7,9],['Luiza',9.5,7.5],['Marcos',6,4],['Luana',5,2.5]]

for i,notas_alunos in enumerate(notas_alunos):
    nome = notas_alunos [0]
    ab1 = notas_alunos [1]
    ab2 = notas_alunos [2]
    media = (ab1 + ab2)/2
    if media >= 7:
        print(f'{notas_alunos [0]}, foi Aprovado')
    else:
        print(f'{notas_alunos [0]}, foi Reprovado')

input('Pressione ENTER para fechar')