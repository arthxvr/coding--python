jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input('Partidas: '))
for c in range(total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {indice+1} fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
