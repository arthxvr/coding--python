lst1 = list(range(1, 11))
lst2 = list(range(10, 0, -1))

for i1, i2 in zip(lst1, lst2):
    print(i1 / i2)
