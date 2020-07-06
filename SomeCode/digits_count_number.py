n = int(input('Enter a number: '))
total = 0
while(n > 0):
    total += 1
    n = n // 10
print(f'The number of digits is: {total}')
