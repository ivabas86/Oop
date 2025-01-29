from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)
        if not isinstance(capacity_volume,(int,float)):
            raise TypeError
        if not isinstance(occupied_volume,(int,float)):
            raise TypeError
        if capacity_volume <= 0 or occupied_volume < 0:
            raise ValueError
        if capacity_volume < occupied_volume:
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    glass = Glass(500,200)
    print(glass.capacity_volume, glass.occupied_volume)
    glass2 = Glass(500, 200)
    print(glass2.capacity_volume, glass2.occupied_volume)
    try:
        ...  # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


