number = int(input('Enter a number: '))
summation = 0
for c in range(1, number + 1):
    summation += c
    if c < number:
        print(f'{c}', end=' + ')
    else:
        print(f'{c}', end=' = ')
print(f'{summation}')
