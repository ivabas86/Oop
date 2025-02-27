# База данных книг для проверки
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
    def __init__(self, id_: int, name: str, pages: int):
        '''

        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге
        '''
        self.id_ = id_
        self.name = name
        self.pages = pages


        if not isinstance(id_, int):
            raise TypeError
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(pages, int):
            raise TypeError

        # TODO дописать метод

    def __str__(self):
        return f'Книга "{self.name}"'

         # TODO дописать метод

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"





if __name__ == '__main__':
    # инициализируем список книг
    book_dict = BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
