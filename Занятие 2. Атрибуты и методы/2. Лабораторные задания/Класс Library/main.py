# База данных книг для проверки
from operator import itemgetter

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


# TODO Импортируйте и скопируйте ранее написанный класс Book

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


class Library:

    def __init__(self, books = None):
        """
        Не забудьте про 'Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь
        его не передал, то библиотека инициализируется с пустым списком книг.'
        :param books: список книг
        """
#         books= [
#     {
#         "id": 1,
#         "name": "test_name_1",
#         "pages": 200,
#     },
#     {
#         "id": 2,
#         "name": "test_name_2",
#         "pages": 400,
#     }
# ]

        # TODO дописать метод
        # if is not isinstance(books,)
        # self.books = books if books is not None else i
        if books is not None:
            self.books = books

            print(self.books)
        else:
            self.books = []


    def get_next_book_id(self):
        """
        Необходимо узнать последнюю книгу в библиотеке, посмотреть атрибут 'id' этой книги и вернуть следующее
        значение после этого `id`
        :return:
        """
        empty_ = []
        if self.books == empty_:
            return 1
        else:
            sl=self.books
            return (sl[-1]['id']+1)



         # TODO дописать метод


    def get_index_by_book_id(self, id_):
        """
        Так как в библиотеке книги хранятся в списке, то данная функция возвращает индекс где книга с определенным
        `id` хранится в списке книг. Для примера. [Book(id=1, ...), Book(id=2, ...)] книга с id=2 хранится
        на индексе 1 списка книг
        :param id_: id книги
        :return: индекс, где лежит книга в списке книг
        """
        # TODO дописать метод
        if id_ is not None:
            if self.books[id_]:
                sl_= self.books[id_]
                return sl_.get('id')
        else:
            raise ValueError('Отсутствует id')




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    book_dict = BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
