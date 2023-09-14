# a = 1 + 1
# c = '1' + '1'
# b = 'Привет' + ' ' + 'мир!'
# print(a)
# print(c)
# print(b)
# print(id(1), type(1))
# print(id(id), type(id))
# print(id(type), type(type))


# a = print
#
# print(5)
# a(5)

#
# class A:
#     def func_1(self):
#         # print(1)
#         self.__func_3()
#         self._func_2()
#
#     def _func_2(self):
#         print(2)
#
#     def __func_3(self):
#         print(3)
#
#
# a = A()
# a.func_1()
# # a._func_2()
# # a._A__func_3()

# print(len([1, 2, 5]))
# print(len('hi'))


# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
#
# print(hasattr(Singleton, 'instance'))
# a = Singleton()
# b = Singleton()
# print(a, id(a))
# print(b, id(b))
# print(hasattr(a, 'instance'))

# def deco(func):             # сама оболочка, всегда на вход получает имя функции
#     # функция - обертка. на вход получает то, что передается главной функции
#     def wrapper(a, b):
#         # return func(a, b) - 1
#         return a * b
#     return wrapper
#
#
# @deco
# def func_1(a, b):
#     return a + b + 1
#
#
# print(f'3 + 3 = {func_1(3, 3)}')

from datetime import datetime


def timeit(func):
    def wrapper(val):
        start = datetime.now()
        rez = func(val)
        end = datetime.now()
        print(f'time: {end - start}')
        return rez
    return wrapper


@timeit
def get_list_1(val):
    lst = []
    for i in range(val):
        if i % 2 == 0:
            lst.append(i)
    return lst


@timeit
def get_list_2(val):
    return [i for i in range(val) if i % 2 == 0]


get_list_1(10000000)
get_list_2(10_000_000)


