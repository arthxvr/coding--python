valor_saque = int(input('Digite o valor que você quer sacar: '))
for notas in (50, 20, 10, 1):
    quantidade = valor_saque // notas
    valor_saque %= notas
    if quantidade > 0:
        print(f'Total de {quantidade} de notas R$:{notas:.2f}')
