def e_triangulo(lado_a, lado_c, lado_C):
    return lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a

def classificar_triangulo(lado_a, lado_b, lado_C):
    if lado_a == lado_b == lado_c:
        return 'Equilátero'
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return 'Isósceles'
    else:
        return 'Escaleno'
    
lado_a = float(input('Digite o lado A: '))
lado_b = float(input('Digite o lado B: '))
lado_c = float(input('Digite o lado C: '))

if e_triangulo(lado_a, lado_b, lado_c):
    tipo = classificar_triangulo(lado_a, lado_b, lado_c)
    print(f'Os valores formam um triângulo {tipo}')
else:
    print('Os valores não formam um triângulo')

input('Precione ENTER para sair')