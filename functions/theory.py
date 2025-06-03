# Higher order function
def outer_fn():
    def inner_fn():
        return "Hello from inner_fn"

    return inner_fn


result = outer_fn()
print(type(result))
print(result())

print(outer_fn()())


# closure
def closure(text):
    msg = text.upper()

    def inner():
        print(msg)

    return inner


closure_fn_result = closure("Hello from closure")
closure_fn_result()  # prints "HELLO FROM CLOSURE"


def increase(counter):
    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


counter_fn = increase(10)
print(counter_fn())
print(counter_fn())
print(counter_fn())
