def vogais(s):
    return [x for x in s if x.lower() in ['a', 'e', 'i', 'o', 'u']]

print(vogais('Arthur'))

