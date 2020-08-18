salario = float(input('Salário do funcionário: R$'))
if salario > 1250.00:
    novo_salario = salario + (salario * 10/100)
    aumento = novo_salario - salario
else:
    novo_salario = salario + (salario * 15/100)
    aumento = novo_salario - salario
print(f'Novo salário: R${novo_salario:.2f}\nAumento de: R${aumento:.2f}')
