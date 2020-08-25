casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de finaciamento: '))

prestacao = casa / (anos * 12)
limite = salario * 30/100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end=' ')
print(f'a prestação será de R${prestacao:.2f}')
if prestacao <= limite:
    print('Empréstimo CONDEDIDO!')
else:
    print(f'Empréstimo NEGADO!')

