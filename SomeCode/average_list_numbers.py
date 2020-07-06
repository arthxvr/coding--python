n = int(input('Enter the number of elements: '))
a = []
for c in range(0, n):
    element = int(input('Enter element: '))
    a.append(element)
    average = sum(a) / n
print('Average of elements in the list', round(average, 2))
