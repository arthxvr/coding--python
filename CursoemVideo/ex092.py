from datetime import date


dados = dict()
dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano_nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - date.today().year
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
