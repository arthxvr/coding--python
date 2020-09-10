lista = []
for c in range(5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1
print(f'Os valores digitados em ordem foram: {lista}')
