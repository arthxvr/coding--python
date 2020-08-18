velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Valor da multa: R${multa:.2f}')  
print('Tenha uma boa viagem, dirija com segurança!')
