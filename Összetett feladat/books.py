import file_handler
import crud_operations
from os import path

PATH = path.join(path.dirname(__file__), 'database', 'books.csv')

books = file_handler.read_file(PATH)


def list_books():
    print(books)


def find_book():
    id = int(input('Add meg a keresendő könyv ID-ját!'))
    print(crud_operations.find_item(id, books))


def update_book():
    id = int(input('Add meg a módosítandó könyv ID-ját!'))
    book = crud_operations.find_item(id, books)
    # title = input('Add meg a könyv új címét!')
    # author = input('Add meg a könyv új szerzőjét!')
    # book.update({'title': title, 'author': author})
    for k in book.keys():
        data = input(f'Add meg a könyv új {k} értékét!: ')
        if data:
            book.update({k: data})
    crud_operations.update_item(id, book, books)
    file_handler.write_file(PATH, books)
    print('Sikeresen frissítettük a könyvet.')


def create_book():
    keys = list(books[0].keys())
    keys.remove('id')
    book = {'id': None}
    for key in keys:
        value = input(f'Add meg az új könyv {key} értékét!: ')
        book.update({key: value})
    crud_operations.create_item(book, books)
    file_handler.write_file(PATH, books)
    print('Az új könyvet létrehoztuk!')


def delete_book():
    id = int(input('Add meg a törölni kívánt könyv ID-ját!'))
    crud_operations.remove_item(id, books)
    file_handler.write_file(PATH, books)
    print('A könyv sikeresen törlésre került.')
