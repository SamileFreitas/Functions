#As maçãs  custam  R$  0,30  cada  se  forem  compradas menos  do  que  uma 
#dúzia,  e  R$0,25  se  forem  compradas  pelo  menos  doze.  Escreva  um 
#programa  que  leia  o  número  de  maçãs  compradas,  calcule  e  escreva  o 
#valor total da compra.

numero_maca = int(input('Digite a quantidade de maças compradas: '))

if numero_maca < 12:
    maca_und = numero_maca * 0.30
    print(f'O valor total da compra de maças é: R$ {maca_und}')
elif numero_maca >= 12:
    maca_duzia = numero_maca * 0.25
    print(f'O valor total da compra de maças é: R$ {maca_duzia}')

#ter cuidado com relação a utilizar ',' pois a linguagem python não premiti e é nessário utilizar '.'
input('Precione ENTER para sair')