def increase_counter(counter):
    counter += 1
    print(counter)


global_counter = 1
increase_counter(global_counter)
print(global_counter)

# IMMUTABLE
# a = 1000
# print(id(a))
# a = 10
# print(id(a))

# b = 1000
# print(id(b))

# b = 1001
# print(id(b))

a = 1000
b = a
print(id(a))
print(id(b))
b = 10
print(id(b))
