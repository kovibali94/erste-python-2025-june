from itertools import count, cycle, repeat, chain, filterfalse, product

# végtelen iterátorok


# def count(start=0, step=1):
#     n = start
#     while True:
#         yield n
#         n += step

iterator_count = (count(10, 10))
print("Even list:", list(next(iterator_count) for _ in range(5)))


# def cycle(iterable):
#     saved = []
#     for element in iterable:
#         yield element
#         saved.append(element)
#     while saved:
#         for element in saved:
#             yield element

iterator_cycle = (cycle('ABCD'))
print("Even list:", list(next(iterator_cycle) for _ in range(10)))


# def repeat(object, times=None):
#     if times is None:
#         while True:
#             yield object
#     else:
#         for i in range(times):
#             yield object

iterator_repeat = (repeat(10))
print("Even list:", list(next(iterator_repeat) for _ in range(10)))


# def chain(*iterables):
#     for it in iterables:
#         for element in it:
#             yield element

# legrövidebb termináló szekvencia
iterator_chain = (chain('ABC', 'DEF'))
print([i for i in iterator_chain])


# def filterfalse(predicate, iterable):
#     if predicate is None:
#         predicate = bool
#     for x in iterable:
#         if not predicate(x):
#             yield x

iterator_filterfalse = (filterfalse(lambda x: x % 5, range(100)))
print([i for i in iterator_filterfalse])


# def product(*args, repeat=1):
#     pools = [tuple(pool) for pool in args] * repeat
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)

# kombinatorika
iterator_product = (product([1, 2, 3], [4, 5, 6]))
print([i for i in iterator_product])
