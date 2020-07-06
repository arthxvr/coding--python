n = int(input('Enter the number: '))
rev = 0
while (n > 0):
    digits = n % 10
    rev = rev * 10 + digits
    n = n // 10
print(f'Number reversed: {rev}')
