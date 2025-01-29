# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Udochka:

    def __init__ (self, length: float, lure_wt: float, missa: float):
        '''

        Инициализация удилища
        :param length: длина удилища
        :param lure_wt: максимальный вес приманки
        :param missa: максимальная нагрузка на удилище


        '''

        if length < 2.5:
            raise ValueError ('Короткое удилище')
        if not isinstance(length, (int, float)):
            raise TypeError('Длина удилища должна быть типа int или float')
        self.length = length
        if lure_wt > 0.25:
            raise ValueError ('Тяжелая приманка')
        if not isinstance(lure_wt, (int, float)):
            raise TypeError('Вес приманки должен быть типа int или float')
        self.lure_wt = lure_wt

        if not isinstance(missa, (int, float)):
            raise TypeError('Вес рыбы должен быть типа int или float')
        if missa > 20:
            raise ValueError ('Тяжелая рыба, удилище сломано')
        self.missa = missa


    def f_use (self, weith: float|int):
        '''
        :param weith: вес рыбы
        :return:
        '''
        if weith > self.missa:
            raise ValueError('Очень большой вес')
        else:
            return weith


    def fishing(self, fish: int|float):
        '''
        Симулирует процесс ловли рыбы и нагрузку на удилище
        :param fish: вес рыбы
        :return: вес рыбы + приманка
        Примеры:
        >>> udochka = Udochka(length=2.7, lure_wt=0.20, missa=19)
        >>> udochka.fishing(6)

        '''
        fish_use = fish + self.lure_wt
        self.f_use(fish_use)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
