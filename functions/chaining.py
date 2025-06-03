def add_cheese(burger):
    burger["cheese"] = True
    return burger


def add_double_meal(burger):
    burger["doubleMeal"] = True
    return burger


def add_bacon(burger):
    burger["bacon"] = True
    return burger


def add_gluten_free(burger):
    burger["glutenFree"] = True
    return burger


def remove_onion(burger):
    burger["onion"] = False
    return burger


def make_burger(base, *args):
    burger = base
    for fn in args:
        burger = fn(burger)
    return burger

custom_burger = make_burger({}, add_cheese, add_double_meal, add_bacon)
print(custom_burger)
