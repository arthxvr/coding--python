expressao = str(input('Digite a expressao: '))
lista = []
for parentesis in expressao:
    if parentesis == '(':
        lista.append('(')
    elif parentesis == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está errada.')
