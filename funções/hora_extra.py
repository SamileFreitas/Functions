"""Calcular hora extra de funcionários"""

#você deve definir as variaveis.
def calc_salario(qt_horas: int, vl_hora: float) -> float:
    if qt_horas > 40:
        #hora comum trabalhada
        hora_comum = 40
        #vai ser hora extra recebe o valor de quantidades de hora trabalhada menos as 40h
        hora_extra = qt_horas - 40
    else:
        hora_comum = qt_horas
        hora_extra = 0
    #para fazer o calculo do salario você deve multiplicar a hora comum e o valor da hora 
    # mais a mutiplicação da hora extra e o valor de cada hora extra
    salario = hora_comum*vl_hora + hora_extra*1.5
    #retornando o salario
    return salario