from typing import Optional


class Product:
    """
    Классовые атрибуты для отслеживания общей информации
        total_products(число): Отслеживает общее количество товаров на складе.
        total_revenue(число): Хранит общую выручку от продаж.
    """
    # TODO Создайте классовые атрибуты total_products (инициализируйте нулем) и total_revenue (инициализируйте нулем)
    total_products = 0
    total_revenue = 0
    def __init__(self, name: str, price: int | float, quantity: int):
        """
        :param name: Название товара
        :param price: Цена товара
        :param quantity: Количество товара на складе
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.add_value_total_products(quantity)

    @classmethod
    def add_value_to_total_revenue(cls, value):
        # TODO Обновите значение классового атрибута total_revenue
        cls.total_revenue += value
    @classmethod
    def add_value_total_products(cls, value):
        # TODO Обновите значение классового атрибута total_products
        cls.total_products +=value

    def sell(self, amount: int) -> None:
        """
        Уменьшает количество товара на указанное значение, обновляет выручку.
        Если количество товара недостаточно, метод должен сообщить об этом, вызвав raise ValueError.
        :param amount: Количество проданного товара
        :return:
        """

        # TODO Проверьте, что если запрашиваемого числа товара нет на складе, то вызывается ошибка ValueError
        if self.quantity < amount:
            raise ValueError
        # TODO Уменьшите количество товара на складе (self.quantity) на соответствующее значение (amount)
                # TODO посчитайте выручку как количество проданного товара умноженное на цену товара
        revenue = amount * self.price
        # TODO Добавить выручку (revenue) к классовой переменной отвечающей за общую выручку
        self.quantity -= amount
        self.add_value_total_products(-amount)
        self.add_value_to_total_revenue(revenue)
        # TODO Уменьшите значение классовой переменной total_products, так как общее чмсор товаров изменилось
        print(f"Продано {amount} шт. товара {self.name}. Выручка: {revenue:.2f}")

    def restock(self, amount: int) -> None:
        """
        Увеличивает количество товара на указанное значение
        :param amount: Количество добавляемого товара
        :return:
        """
        # TODO Увеличьте количество товара на складе (self.quantity) на соответствующее значение (amount)'
        self.quantity += amount
        Product.total_products +=amount
        # TODO Увеличьте общее число товаров total_products (классовый атрибут)
        print(f"Поступило {amount} шт. товара {self.name}. Всего на складе: {self.quantity}")

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Store:
    def __init__(self, name: str, products: Optional[list[Product]] = None):
        self.name = name
        self.products = products if products is not None else []

    def total_inventory(self):
        """
        Возвращает общее количество всех товаров в магазине.
        :return:
        """
        # TODO Верните общее количество всех товаров в магазине.
        return sum(map(lambda x: x.quantity, self.products))
    def total_value(self):
        """
        Возвращает общую стоимость всех товаров в магазине.
        :return:
        """
        # TODO Верните общую стоимость всех товаров в магазине.
        return sum([prod.price * prod.quantity for prod in self.products])
        # return sum(map(lambda x: x.price * x.quantity, self.products))
    @staticmethod
    def compare_prices(product1: Product, product2: Product):
        # TODO Реализуйте сравнивание цен. Верните название товара с большей ценой, если одинаковые, то верните 'Цены одинаковы'.
        if product1.price > product2.price:
            return product1.name
        elif product1.price == product2.price:
            return ('цены одинаковы')
        else:
            return product2.name

if __name__ == "__main__":
    apple = Product("Apple", 1.5, 100)
    banana = Product("Banana", 0.9, 150)
    cherry = Product("Cherry", 3.0, 50)

    store = Store("My Grocery Store", [apple, banana, cherry])

    print(store.total_inventory())  # Вывод: 300
    print(store.total_value())  # Вывод: 435.0

    apple.sell(30)
    print(Product.total_revenue)  # Вывод: 45.0

    print(Store.compare_prices(apple, banana))  # Вывод: Apple

    print(store.total_inventory())  # Вывод: 270
    print(store.total_value())  # Вывод: 390.0
