def kwargs(**kwargs):
    print(kwargs)
    return kwargs


result = kwargs(language="Python", version=3.13, author="John Doe")
print(type(result))


def generate_filter_query(**kwargs):
    query = "SELECT * FROM products WHERE "
    for k, v in kwargs.items():
        query += f"{k}='{v}' AND "
    return query[:-5]


print(generate_filter_query(category="electronics", brand="BrandX", color="black"))
