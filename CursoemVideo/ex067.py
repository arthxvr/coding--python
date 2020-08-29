cont = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{num} x {cont} = {num * cont}')
    cont = 0
    print('-=' * 15)
print('Finalizando algoritmo...')
