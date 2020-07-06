n = int(input('Enter a number: '))
total = 0
while (n > 0):
    digits = n % 10
    total += digits
    n = n // 10
print(f'The sum of digits is {total}')
