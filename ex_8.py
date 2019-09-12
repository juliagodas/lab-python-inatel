velocidade=float(input('velocidade do carro: '))

if velocidade == 80:
    print ('Tenha uma Boa viagem!')
else:
    print ('Você foi multado no valor de R$ 50,00 a cada KM ultrapassado.')
    multa = (velocidade-80)*50
    print ('O valor de sua multa é R$: ',multa)

    