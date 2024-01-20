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

class Library:
    def __init__(self, books=None):
        self.books = books
        if books is None:
            self.books = []

    def get_next_book_id(self) -> int:
        if not(self.books):
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id: int) -> int:
        if not isinstance(id, int):
            raise TypeError("Индекс должен быть типа int")
        index = id
        enum = enumerate(self.books, 1)
        for item in enum:
            if item[0] == index:
                return item[0]-1 #так как индексация списка с нуля, а нумерация id с единицы, то для получения индекса книги достаточно уменьшить айди на 1
        return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
