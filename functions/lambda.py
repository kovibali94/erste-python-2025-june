from functools import reduce


def increase_by_one(x):
    return x + 1


# ruff: noqa: E731
increase_by_one_lambda = lambda x: x + 1


def make_inc(x):
    return lambda y: x + y


result_fn = make_inc(10)
print(result_fn(5))
print(result_fn(50))

net_prices = [100, 200, 300, 400, 500]
gross_prices = list(map(lambda price: price * 1.27, net_prices))
print(gross_prices)


def complex_fn(x):
    pass


filtered_prices = list(filter(lambda price: price > 200, net_prices))
print(filtered_prices)

total_price = reduce(lambda x, y: x + y, net_prices)
print(total_price)

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# filter even numbers, double them, and sum them up
result = reduce(
    lambda x, y: x + y, map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums))
)
print(result)

result_comp = sum(i for i in nums if i % 2 == 0) * 2
print(result_comp)
