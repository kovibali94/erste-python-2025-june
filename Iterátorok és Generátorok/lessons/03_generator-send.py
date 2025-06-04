def square_inputs():
    while True:
        num = yield
        yield num**2


gen = square_inputs()
next(gen)
print(gen.send(10))

next(gen)
print(gen.send(50))

next(gen)
print(gen.send(100.25))
