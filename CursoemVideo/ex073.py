times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
         'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
         'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
         )
print('-=' * 50)
print(f'5 primeiros colocados: {times[0:5]}')
print('-=' * 50)
print(f'4 últimos colocados: {times[-4:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'O time Chapecoense está na posição: {times.index("Chapecoense")+1}')
print('-=' * 50)
