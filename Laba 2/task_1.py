BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError("ID должно быть типа int")
        self.id = id
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        self.pages = pages
    def __str__(self):
        return 'Книга "' + self.name + '"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__
    print(list_books)  # проверяем метод __repr__
