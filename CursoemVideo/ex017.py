from math import hypot


co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'A hipotenusa é: {hipotenusa:.2f}')
