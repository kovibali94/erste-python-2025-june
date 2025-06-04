import math


def log_args(*args):
    return args


result = log_args(1, 2, 3, "a", "b", "c")
print(type(result))


def talk(name, *args):
    print(f"Hello {name}. - {' '.join(args)}")


talk("Alice", "How are you?", "I hope you're doing well.")


def generate_square_matrix(*numbers):
    matrix = []
    size = math.floor(math.sqrt(len(numbers)))
    for i in range(0, len(numbers), size):
        matrix.append(list(numbers[i : size + i]))
    return matrix


print(generate_square_matrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
