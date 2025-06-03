salaries = [1000, 2000, 3000, 4000, 5000]
salaries_copy = salaries

print(id(salaries))
print(id(salaries_copy))

salaries.append(6000)

print(salaries)
print(salaries_copy)

salaries_copy.append(7000)
print(salaries)
print(salaries_copy)


def add_salary(salaries_list, salary):
    salaries_list.append(salary)


add_salary(salaries, 8000)
print(salaries)
print(salaries_copy)

salaries_copy = [1, 2, 3, 4]
print(salaries)
print(salaries_copy)

# str = "Hello"
# print(str[0])
# str[0] = "h"

salaries_copy_2 = salaries.copy()  # salaries[:]
print(id(salaries))
print(id(salaries_copy_2))
