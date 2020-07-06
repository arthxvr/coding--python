n = int(input('Enter an integer number: '))
a = []
for c in range(2, n + 1):
    if n % c == 0:
        a.append(c)
    a.sort()
print(f'The smallest divisor is: {a[0]}')
