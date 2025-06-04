square_generator = (i**2 for i in range(3))
a, b, c = square_generator

print(a, b, c)

print(*(x for x in range(10)),)
print(type(x for x in range(10)))
