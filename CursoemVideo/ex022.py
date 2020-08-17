nome = str(input('Nome completo: ')).upper().strip()
print(f'Nome em maísculas: {nome}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Letras ao todo: {len(nome) - nome.count(" ")}')
print(f'Letras do primeiro nome: {len(nome.split()[0])}')


