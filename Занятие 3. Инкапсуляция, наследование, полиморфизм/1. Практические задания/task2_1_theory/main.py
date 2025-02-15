# # TODO скопириуйте и запустите здесь необходимый код
# class A:
#     class_attr = 10  # классовый атрибут
#
#     def __init__(self, param):
#         self.param = param  # экземплярный атрибут
#
#
#     @classmethod
#     def change_class_attr(cls, value):
#             cls.class_attr = value
#
#     def get_param(self):  # экземплярный метод
#         return self.param
#
#
#
# class B(A):  # Так происходит наследование, теперь в классе B есть все тоже самое, что и в классе A
#     new_attr = 'Это классовый атрибут класса B'
#
#     @staticmethod
#     def hello():  # Добавили метод которого не было в классе A
#         print("Привет из класса B")
class A:
    attr_A = 10

    def __init__(self, param_a):
        self.param_a = param_a

    def method_a(self):
        return 'A'


class B:
    attr_B = 20

    def __init__(self, param_b):
        self.param_b = param_b

    def method_b(self):
        return 'B'


class C(A, B):  # Множественное наследование
    attr_С = 30

    def method_c(self):
        return 'C'


# if __name__ == "__main__":
#     obj_a = A(20)
#     obj_b = B(40)  # хотя мы и не писали __init__(self, param) в классе B, но оно полностью скопировалось из класса A
#
#     print(obj_a.get_param())  # 20
#     print(obj_b.get_param())  # 40  Скопировали все методы
#
#     print(obj_a.class_attr)  # 10
#     print(obj_b.class_attr)  # 10 Атрибуты тоже скопировались
#
#     obj_a.change_class_attr(20)  # Изменили классовый атрибут класса А
#     obj_b.change_class_attr(30)  # Изменили классовый атрибут класса B
#
#     print(obj_a.class_attr)  # 20
#     print(obj_b.class_attr)  # 30  Копирование есть копирование, даже классовых атрибутов, они теперь независимые
#     print(obj_b.class_attr)  # 10 Есть атрибут скопированный из класса А
#     print(obj_b.new_attr)  # 'Это классовый атрибут класса B' и новый атрибут которого нет в классе A
#
#     print(obj_b.get_param())  # 40 Есть метод скопированный из класса А
#     obj_b.hello()  # "Привет из класса B" и новый метод которого нет в классе A

if __name__ == "__main__":
    obj_c = C(30)  # def __init__ тоже скопировался, но с какого класса?

    print(obj_c.param_a)  # 30 Скопировался только __init__ с класса A, так как при одинаковых названиях оставляется
    # тот чей класс левее при наследовании
    try:
        print(obj_c.param_b)
    except AttributeError as err:
        print(err)  # 'C' object has no attribute 'param_b'

    # Остальные методы и атрибуты скопировались полностью, так как их названия не повторяются
    print(obj_c.method_a(), obj_c.method_b(), obj_c.method_c())  # A B C
    print(obj_c.attr_A, obj_c.attr_B, obj_c.attr_С)  # 10 20 30