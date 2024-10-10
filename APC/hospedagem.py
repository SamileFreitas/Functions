quant_hospede = int(input('DIgite quantos dias o hóspede irá ficar no hotel: '))
valor_diaria = 150

if quant_hospede <= 0:
    print('Quantidade de dias inválido')
elif quant_hospede > 5:
    diaria = (valor_diaria + 7.5) * quant_hospede
    print(f'Valor a ser cobrado por {quant_hospede} da diária, é no valor de: R$ {diaria} reais.')
elif quant_hospede == 5:
    diaria = (valor_diaria + 9) * quant_hospede
    print(f'Valor a ser cobrado por {quant_hospede} da diária, é no valor de: R$ {diaria} reais.')
else:
    quant_hospede < 5
    diaria = (valor_diaria + 10.50) * quant_hospede
    print(f'Valor a ser cobrado por {quant_hospede} da diária, é no valor de: R$ {diaria} reais.')

input('Precione ENTER para sair')