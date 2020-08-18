def fibonacci(n):
    if type(n) != int:
        raise TypeError('n must be a positive int') 
    if n < 1:
        raise ValueError('n must be a positive int')
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for c in range(1, 50):
    print(c, ":", fibonacci(c))
