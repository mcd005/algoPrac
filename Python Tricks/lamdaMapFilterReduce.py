#lambda arguments : expression to be returned
add5 = lambda x : x + 5

#Can be used recursively
fact = lambda x: 1 if x == 0 or x == 1 else x * fact(x - 1)

#Typically used for sorting
list1 = [('eggs', 5.25), ('honey', 9.70), ('carrots', 1.10), ('peaches', 2.45)]
list1.sort(key = lambda x: x[1])
# print(list1)

#Or filtering
list1 = [1, 2, 3, 4, 5, 6]
list2 = list(filter(lambda x: x%2 == 0, list1))
# print(list2)

import math

def area(r):
    return math.pi * (r**2)

radii = [6, 7, 10, 13]

print(list(map(area, radii)))

print(list(filter(lambda a: a > 300, map(area, radii))))