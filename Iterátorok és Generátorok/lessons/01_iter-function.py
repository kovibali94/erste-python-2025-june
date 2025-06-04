name = 'John Doe'
my_str_iterator = iter(name)

print(next(my_str_iterator))
print(next(my_str_iterator))
print(next(my_str_iterator))


roles = ('user', 'admin', 'sysadmin')
roles_iterator = iter(roles)
# print(next(roles_iterator))
# print(next(roles_iterator))
# print(next(roles_iterator))

for role in roles_iterator:
    print(role)

# StopIteration
print(next(roles_iterator))
