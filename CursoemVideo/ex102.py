def fatorial(n, show=False):
    fat = 1
    c = n
    while c > 0:
        if show:
            if c > 1:
                print(c, 'x ', end='')
            else:
                print(c, '= ', end='')
        fat *= c
        c -= 1
    return fat
print(fatorial(6, show=True))
