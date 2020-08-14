def primo(n):
    for c in range(2, n):
        if n % c == 0:
            return False
    return n > 1

print(list(filter(primo, range(0, 101))))
