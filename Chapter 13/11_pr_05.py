from functools import reduce
l = [3, 10, 455, 2, 5, 1, 456]

a = reduce(max, l)
print(a)
