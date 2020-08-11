for c in range(1, 51):
    if c % 3 == 0 and c % 5 == 0:
        print(c, '- FizzBuzz')
    elif c % 5 == 0:
        print(c, '- Buzz')
    elif c % 3 == 0:
        print(c, '- Fizz')
