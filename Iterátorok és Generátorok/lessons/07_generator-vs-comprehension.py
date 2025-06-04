import sys

# <generator object <genexpr> at 0x106ecc580>
# does not compute values
# Memory error possibility

nums_generator = (i * i for i in range(100_000_000))

print('nums_generator size in bytes: ',sys.getsizeof(nums_generator))  # 208 bytes
# can only be iterated once
print('sum: ', sum(nums_generator))
# 0
print('sum second run: ', sum(nums_generator))

nums_list_comprehension = [i * i for i in range(100_000_000)]

print('list comprehension size in bytes: ', sys.getsizeof(nums_list_comprehension))  # 835128600 bytes
print(sum(nums_list_comprehension))
