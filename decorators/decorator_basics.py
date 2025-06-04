def basic_decorator(fn):
    def wrapper():
        print("Start wrapper")
        fn()
        print("Stop wrapper")

    return wrapper


@basic_decorator
def say_hello():
    print("Hello, world!")

say_hello()

# decorated_say_hello = basic_decorator(say_hello)
# decorated_say_hello()
