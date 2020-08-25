num = int(input('Digite um número para calcular o seu fatorial: '))
cont = num
fatorial = 1
while cont > 0:
    print(cont,end=' ')
    if cont > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    fatorial *= cont
    cont -= 1
print(fatorial)
