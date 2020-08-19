preco = float(input('Preço do produto: R$'))
print('''Condições de pagamento:
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: Preço normal
[ 4 ] 3x ou mais: no cartão: 20% de juros
      ''')
opcao = int(input('Opção desejada: '))
if opcao == 1:
    novo_preco = preco - (preco*10/100)
    print(f'Preço do produto com 10% de desconto: R${novo_preco:.2f}')
elif opcao == 2:
    novo_preco = preco - (preco*5/100)
    print(f'Preço do produto com 5% de desconto: R${novo_preco:.2f}')
elif opcao == 3:
    novo_preco = preco * 0.50
    print(f'Preço do produto: 2x de R${novo_preco:.2f}')
elif opcao == 4:
    novo_preco = preco + (preco*20/100)
    print(f'Preço do produto em 3x ou mais no cartão: R${novo_preco:.2f} ')
else:
    print('Opção inválida!')
