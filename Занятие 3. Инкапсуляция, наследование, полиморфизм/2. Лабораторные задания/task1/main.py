
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        # self.name = name
        # self.author = author
        super().__init__(name, author)
        self.pages = pages



    @property
    def pages(self)-> int:
        return self.pages

    @pages.setter
    def pages(self,value: int):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError


    def __str__(self):
        return (super().__str__() + f" Страницы {PaperBook.pages}")


    def __repr__(self):
        return (super().__str__() + f" {self.__class__.__name__}(pages={self.pages!r})")

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        # self.name = name
        # self.author = author
        self.duration = duration

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError
        if value < 0:
            raise ValueError

    def __str__(self):
        return (super().__str__() + f" Объем {AudioBook.duration}")

    def __repr__(self):
        return (super().__str__() + f" {self.__class__.__name__}(pages={self.duration!r})")

if __name__ == "__main__":
    book = Book('Капитанская дочь', 'Пушкин')
    paperbook = PaperBook ('Капитанская дочь', 'Пушкин',430)
    audiobook = AudioBook ('Война и мир', 'Толстой',4.3)
    print(paperbook)
    print(audiobook)