def basic_decorator(fn):
    def wrapper(name):
        print("Start wrapper")
        fn(name)
        print("Stop wrapper")

    return wrapper


@basic_decorator
def say_hello(name):
    print(f"Csáó {name}!")


say_hello("Gergő")
