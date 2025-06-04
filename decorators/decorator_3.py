def apply_tax(tax):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            # result = fn(*args, **kwargs)
            # increase_value = result * (1 + tax / 100)
            # return increase_value
            return fn(*args, **kwargs) * (1 + tax / 100)

        return wrapper

    return decorator


def apply_discount(discount):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * (1 - discount / 100)

        return wrapper

    return decorator


@apply_tax(5)
def summa(a, b):
    return a + b


@apply_discount(20)
@apply_tax(10)
def get_price(price):
    return price


print(summa(100, 200))
print(get_price(100))
