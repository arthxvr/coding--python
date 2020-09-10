from colorama import init


init()
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        print('\033[32mValor adicionado com sucesso.\033[m')
        lista.append(valor)
    else:
        print('\033[31mValor duplicado não adicionado.\033[m')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
print(f'Você digitou os valores: {lista}')
