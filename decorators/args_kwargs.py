# item = {"name": "apple", "price": 1.5, "quantity": 3}
def calculate_total_price(*items, **kwargv):
    total = sum(item["price"] * item["quantity"] for item in items)
    if "discount" in kwargv:
        total *= (100 - kwargv["discount"]) / 100
    if "vat" in kwargv:
        total *= (100 + kwargv["vat"]) / 100
    return total


total = calculate_total_price(
    {"name": "apple", "price": 1.5, "quantity": 3},
    {"name": "banana", "price": 0.8, "quantity": 5},
    {"name": "orange", "price": 2.9, "quantity": 8},
    discount=10,
    vat=20,
)

print(total)

# Better real life example
# def total(basket, vat_percent=27, discount_percent=0):
#     total = sum(item["price"] * item["quantity"] for item in basket)
#     if discount_percent:
#         total *= (100 - discount_percent) / 100
#     if vat_percent:
#         total *= (100 + vat_percent) / 100
#     return total
