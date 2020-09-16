def cadastrar(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

nome_jogador = str(input('Nome do jogador: '))
gols_jogador = str(input('Número de gols: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador.strip() == '':
    cadastrar(gol=gols_jogador)
else:
    cadastrar(nome_jogador, gols_jogador)
