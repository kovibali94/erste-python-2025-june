first_name = "John"
last_name = "Doe"
age = 33
status = "dead"

first_name, last_name, age, status = "John", "Doe", 33, "dead"

a = "a"
b = "b"

# tmp = a
# a = b
# b = tmp

a, b = b, a
print(a, b)


# unpacking string
str = "Hello"
first_chr, second_chr, third_chr, fourth_chr, fifth_chr = str
print(first_chr, second_chr, third_chr, fourth_chr, fifth_chr)

first_chr, *rest = str
print(first_chr, rest)

first_chr, *rest, last_chr = str
print(first_chr, rest, last_chr)

# unpacking list
my_list = [1, 2, 3, 4, 5]
first_elem, *rest, last_elem = my_list
print(first_elem, rest, last_elem)

# unpacking dict
my_dict = {"name": "John", "age": 33, "status": "dead"}
name, age, *rest = my_dict.values()
print(name, age, rest)
