altura = float(input('Altura da parede(m): '))
largura = float(input('Largura da parede(m): '))
area = altura * largura 
litros = area / 2
print(f'Dimensão da parede: {altura}x{largura} | Área: {area}m²')
print(f'Litros de tinta: {litros}l')
