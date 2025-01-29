import doctest
from random import random, choice
from typing import Union


class Auto_:
     global colors_bank
     colors_bank = ['красный','черный','зеленый', 'белый', 'синий']
     def __init__(self,
                  model: str = None,
                  car_brand: str = None,
                  color: str = None):
         '''

         :param model: модель автомашины
         :param car_brand: брэнд автомашины
         :param color: цвет автомашины
         Примеры:
         >>> auto = Auto_(model= 'GT', car_brand= 'Volga', color= 'белый')
         >>> auto.paint_peeled_off = True
         '''

         if not isinstance(car_brand,str):
             raise TypeError('Необходимо ввести буквы')
         self.car_brand = car_brand
         if not isinstance(model,str):
             raise TypeError('Необходимо ввести буквы')
         self.model = model
         if not isinstance(color,str):
             raise TypeError('Необходимо ввести буквы')
         self.color = color
         self.paint_peeled_off = False


     def remove_paint (self):
         '''
         :return: удаляет цвет и возвращает цвет "None"
         Примеры:
         >>> auto = Auto_(model= 'GT', car_brand= 'Volga', color= 'белый')
         >>> auto.paint_peeled_off = True
         >>> auto.remove_paint()

         '''

         if  self.paint_peeled_off is True:
             self.color = None
             self.get_color(self.color)


     def get_color (self, colort: str|None):
         '''
         :param colort: принимает данные о цвете
         :return: возвращает цвет для покраски автомашины
         Примеры:
         >>> auto = Auto_(model= 'GT', car_brand= 'Volga', color= 'белый')
         >>> auto.paint_peeled_off = True
         >>> auto.remove_paint()
         >>> auto.get_color(None)

         '''
         if colort is None and self.paint_peeled_off is True:
             for s in colors_bank:
                 if colors_bank.index(s) != colors_bank.index('белый'):
                     col = choice(colors_bank)
                     self.paint_color(col)


     def paint_color(self,colort: str):
         '''

         :param colort: получение цвета для перекраски автомашины
         :return: Автомашина покрашена в полученный цвет
         Примеры:
         >>> auto = Auto_(model= 'GT', car_brand= 'Volga', color= 'белый')

         '''
         self.color = colort


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    # auto = Auto_(model= 'GT', car_brand= 'Volga', color= 'белый')
    # print(f'Автомашина брэнда {auto.car_brand} модели {auto.model} и цветом {auto.color}')
    # auto.paint_peeled_off = True # Покрытие автомашины повреждено
    # print('После повреждения автомашины необходимо удалить старую краску')
    # auto.remove_paint() #необходимо удалить старую краску
    # print(f'Краска с покрытия автомобиля удалена, покрытие автомашины перекрашено в цвет: {auto.color}')


