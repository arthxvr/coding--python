dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = dias*60+km*0.15 
print(f'Total a pagar: R${total:.2f}')
