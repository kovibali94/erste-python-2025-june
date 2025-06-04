def generate_ids():
    yield 1
    yield 2
    yield 3


id_generator = generate_ids()
print(id_generator)

# step by step
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
# StopIteration
# print(next(id_generator))

# iterate over
for i in generate_ids():
    print(i)

# generator expression, NOT a tuple
id_generator_2 = (num for num in range(1, 4))
for id in id_generator_2:
    print(id)
