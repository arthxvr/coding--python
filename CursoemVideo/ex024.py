cidade = str(input('Cidade: ')).strip()
verificacao = cidade.split()[0].upper() in 'SANTO'
print(f'A cidade começa com SANTO? {verificacao}')
