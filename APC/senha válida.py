#Escreva  um  programa  que  verifique  a  validade  de  uma  senha  fornecida pelo  usuário.  A  senha  válida  é  o  número  1234. 
# Devem  ser impressas  as seguintes mensagens: ACESSO PERMITIDO caso a senha seja válida. ACESSO NEGADO caso a senha seja inválida.

senha = input('Digite a senha de usuário: ')
senha_valida = '1234'

if senha == senha_valida:
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')

input('Precione ENTER para sair')