from colorama import init


init()
def leiaInt(msg):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return num


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
