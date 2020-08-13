
meio = lambda s: s[round((len(s)/2)+0.1)-1] if len(s) % 2 == 1 else ''
print(meio('SQL'))
