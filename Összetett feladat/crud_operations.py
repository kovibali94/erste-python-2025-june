def create_item(item, items):
    # if items is ampty list, set id to 1
    item.update({'id': items[-1]['id'] + 1})
    items.append(item)
    return items[-1]


def find_item(id, items):
    for item in items:
        if item['id'] == id:
            return item
    return None


def update_item(id, updated_item, items):
    item = find_item(id, items)
    if item is not None:
        index = items.index(item)
        items[index].update(updated_item)
        return items[index]
    return None


def remove_item(id, items):
    item = find_item(id, items)
    if item is not None:
        items.remove(item)
