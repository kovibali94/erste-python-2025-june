net_prices = [price for price in range(100, 1000, 100)]
gross_prices = [price * 1.27 for price in net_prices]

# gross_prices = []

# for price in net_prices:
#     gross_prices.append(price * 1.27)

print(gross_prices)

numbers = [number for number in range(1, 11)]
print(numbers)
odd_numbers = [number for number in numbers if number % 2 != 0]

# odd_numbers=[]
# for number in numbers:
#     if number % 2 != 0:
#         odd_numbers.append(number)

print(odd_numbers)

matrix = [[val for val in range(6)] for _ in range(3)]
print(matrix)

rpg_games = [
    ["Earthdawn", "M.A.G.U.S", "D&D"],
    ["Cyberpunk", "Shadowrun", "Rifts"],
    ["Vampire", "Call of Cthulhu"],
]

rpg_games_flat = [game for sublist in rpg_games for game in sublist]
print(rpg_games_flat)

int_tuple = (1,)
print(type(int_tuple))
