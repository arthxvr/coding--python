numero = int(input('Número inteiro: '))
print('''
[1] para binário
[2] para octal
[3] para hexadecimal
''')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'{numero} é igual {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} é igual {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} é igual {hex(numero)[2:]}')
else:
    print('Opção inválida!')
