number = int(input('Enter number: '))
temporary = number
rev = 0 
while number > 0:
    digits = number % 10
    rev = rev * 10 + digits
    number = number // 10
if (temporary == rev):
    print(f'The number is palindrome')
else:
    print(f'The number isn\'t a palindrome')

