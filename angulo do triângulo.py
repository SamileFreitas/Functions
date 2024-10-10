#Escreva  um  programa  que  leia  o  valor  de  3  ângulos  de  um  triângulo  e escreva  se  o  triângulo  é  Acutângulo,  
# Retângulo  ou  Obtusângulo.  Sendo que: 

angulo1 = int(input('Digite o angulo1 do triângulo: '))
angulo2 = int(input('Digite o angulo2 do triângulo: '))
angulo3 = int(input('Digite o angulo3 do triângulo: '))

#verificar se é um triângulo
if angulo1 + angulo2 + angulo3 == 180:

    #decide o tipo de triângulo
    #Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
    if angulo1 == 90 or angulo2 == 90 or angulo3 ==90:
        print('Este é um triângulo retângulo.')
    #Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º) 
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print('Este é um triângulo Obtusângulo.')
    else:
       #Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
        print('Este é um triângulo Acutângulo.')
else:
    print('O ângulo informado não forma uma triângulo.')

input('Precione ENTER para sair')