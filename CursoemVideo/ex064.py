n = cont = soma = 0
limite = False
while not limite:
    soma += n
    cont += 1
    n = int(input('Digite um valor[999 para parar]: '))
    if n == 999:
        limite = True
print(f'Foram digitados: {cont} números.')
print(f'A soma entre eles é: {soma}')
