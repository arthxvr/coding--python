palavras = ('aprender', 'programar', 'liguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos as vogais', end=' ')
    for letra in i:
        if letra.lower() in 'aáêeéêiíoóu': 
            print(letra, end=' ')    
