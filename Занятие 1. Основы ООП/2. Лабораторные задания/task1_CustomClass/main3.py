import doctest
from random import random, choice
from typing import Union


class computer_:
     def __init__(self,
                  processor: str = '3.6 Ghz',
                  brand: str = 'Intel',
                  monitor: str = 17,
                  energy_on: int = None):
         '''

         :param processor: скорость процессора
         :param brand: брэнд
         :param monitor: размер экрана монитора
         :param energy_on: напряжение
         Примеры:
         >>> computer = computer_(energy_on = 220)
         >>> computer.energy_on
         220
         '''
         if not isinstance(brand,str):
             raise TypeError('Необходимо ввести буквы')
         self.brand = brand

         if not isinstance(processor,str):
             raise TypeError('Необходимо ввести буквы')
         self.processor = processor

         if not isinstance(monitor,int):
             raise TypeError('Необходимо ввести цифры')
         if 14 > monitor > 17:
             raise ValueError ('Отсутствует монитор с таким параметром')
         self.monitor = monitor

         if not isinstance(monitor,int):
             raise TypeError('Необходимо ввести цифры')
         if 220 > energy_on > 220:
             raise ValueError ('Отсутствует напряжение или превышает максимальный параметр')
         self.energy_on = energy_on


     def energy (self):
         '''
         :return: передает напряжение монитору и процессору
         Примеры:
         >>> computer = computer_(energy_on = 220)
         >>> computer.energy_on == 220
         True
         '''

         if self.energy_on != 220:
             raise ValueError ('Недостаточно напряжения или превышается необходимое значение')
         self.monitor_on(self.energy_on)
         self.processor_on(self.energy_on)

     def monitor_on(self, energy):
         '''

         :param energy: поступает напряжение 220
         :return: монитор работает
         Примеры:
         >>> computer = computer_(energy_on = 220)
         >>> computer.monitor_on(220)
         True
         '''
         if self.monitor is None:
             raise ValueError('Отсутствует монитор')
         while energy == 220:
             return True


     def processor_on (self, energy: int):
         '''

         :param energy: поступает напряжение 220
         :return: процессор работает
         >>> computer = computer_(energy_on = 220)
         >>> computer.processor_on(220)
         True
         '''
         if self.processor is None:
             raise ValueError('Отсутствует процессор')

         while energy == 220:
             return True



     def computer_on(self):
         '''
         :return: Подтверждение работы процессора и монитора, значит работает компьютер
         Примеры:
         >>> computer = computer_(energy_on = 220)
         >>> computer.computer_on()
         Компьютер работает
         '''
         if self.monitor_on and self.processor_on:
             print("Компьютер работает")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()



