n = cont = soma = 0
n = int(input('Digite um valor[999 para parar]: '))
while numero != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor[999 para parar]: '))
print(f'Foram digitados: {cont} números.')
print(f'A soma entre eles é: {soma}')
