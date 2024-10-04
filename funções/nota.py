def min_max(notas_alunos):
    nota_min = notas_alunos[0]
    nota_max = notas_alunos[0]

    for nota in notas_alunos:
        if nota < nota_min:
            nota_min = nota
        if nota > nota_max:
            nota_max = nota
    return nota_min, nota_max

def calc_nota(nota, nota_min, nota_max):
    #notas iguais
    if nota_max == nota_min:
        return 10
    return ((nota - nota_min) / (nota_max - nota_min)*10)

def ajustar_notas(notas_alunos):
    nota_min, nota_max = min_max(notas_alunos)
    notas_ajust = []

    for nota in notas_alunos:
        notas_ajust += [calc_nota(nota, nota_min, nota_max)]

    return notas_ajust
