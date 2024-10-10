#Escreva  um  programa  para  ler  o  ano  de  nascimento  de  uma  pessoa  e escrever  uma  mensagem  
# que  diga quantos dias essa pessoa já viveu (considerar que meses tem 30 dias).

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_nascimento
dias_vividos = idade * 12 * 30
print(f"Você já viveu aproximadamente {dias_vividos} dias.")

input('Precione ENTER para sair')