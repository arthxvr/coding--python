total_gasto = mais_caros = menor_preco  = cont = 0
nome_barato = ''
while True:
    print(f"-=" * 20)
    print(f"{' LOJA BARATINHO ':-^40}")
    print(f"-=" * 20)
    produto = str(input("Nome do produto: "))
    preco = float(input('Preço do produto: R$'))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        mais_caros += 1
    elif cont == 1 or preco < menor_preco:
            menor_preco = preco
            nome_barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'Total gasto na compra: R$: {total_gasto:.2f}')
print(f'Total de produtos custando mais de R$1000.00: {mais_caros}')
print(f'{nome_barato} é o produto mais barato e custa R${menor_preco:.2f}')
