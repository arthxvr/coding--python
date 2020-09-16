def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)
