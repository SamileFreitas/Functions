#importação da função
from funções.boas_vindas import bem_vindo

print('Sistema')
nome = input('Digite seu nome para iniciar: ')

bem_vindo(nome)

input('Pressione ENTER para sair.')