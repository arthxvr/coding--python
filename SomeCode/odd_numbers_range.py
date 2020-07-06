lower_limit = int(input('Enter the lower limit for the range: '))
upper_limit = int(input('Enter the upper limit for the range: '))
for c in range(lower_limit, upper_limit + 1):
    if c % 2 != 0:
        print(c, end=' ')

