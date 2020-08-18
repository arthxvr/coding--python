km = float(input('Distância da viagem(km): '))
if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45
print(f'\nDistância da viagem: {km}km/h\nValor da passagem: R${passagem:.2f}')
