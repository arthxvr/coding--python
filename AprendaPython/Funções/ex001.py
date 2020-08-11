def obter_dominio(s):
    return s.split('@')[-1]
print(obter_dominio('myemail@mydomain.com'))
