"""Calcular imposto, atraves de uma função generica"""
        #não utilizar o for dentro de funções

def calcular_imposto(salario_fun: float) -> float:
    if salario_fun >= 1500:
        #apos uma definição retorna da maneira correto para a variavel
        return 0.27*salario_fun
    #no lugar de utilizar else, posso utilizar "return" para caso o if não ser necessário inserir outro exemplo.
    return 0