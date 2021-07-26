# WAP to find the max. of the numbers in a list using the reduce function.

from functools import reduce
l = [3, 8, 455, 2, 5, 4545]

a = reduce(max, l)
print(a)