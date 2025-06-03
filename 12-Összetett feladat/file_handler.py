def read_file(filepath):
    with open(filepath, 'r') as file:
        books = []
        for line in file:
            id, title, author = line.rstrip().split(';')
            books.append({
                'id': int(id),
                'title': title,
                'author': author,
            })
        return books


def write_file(filepath, books):
    with open(filepath, 'w') as file:
        for book in books:
            row = ';'.join(str(val) for val in book.values()) + '\n'
            # remove the last character from the string
            file.write(row)
