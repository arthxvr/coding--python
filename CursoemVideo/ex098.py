from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for contagem in range(inicio, fim+1, passo):
            print(contagem, end=' ', flush=True)
            sleep(0.5)
    elif inicio > fim:
       for contagem in range(inicio, fim-1, -passo):
           print(contagem, end=' ', flush=True)
           sleep(0.5)
    print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada: ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
