def votar(ano_nasc):
    from datetime import date
    
    
    idade = date.today().year - ano_nasc
    if idade < 16:
        return f' Com {idade} anos: VOTO NEGADO'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO'


ano_nasc = int(input('Ano de Nascimento: '))
print(votar(ano_nasc))
