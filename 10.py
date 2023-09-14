# def func(a):
#     print(f'{a}^2 = {a ** 2}')
#
#
# def func_2(a):
#     print(f'{a}^2 = {a ** 2}')
#     return a ** 2
#
#
# print(func(5))
# print(func_2(5))

# from pprint import pprint


# class Human:
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#
# human_1 = Human(name='Ваня', height=180, weight=80)
# human_2 = Human('Петя', 160, 80)
# human_1.height = 182
# print(f'{human_1.name} весит {human_1.weight} кг. при росте {human_1.height} см.')
# print(human_2.name)


import random


class Tank:
    """Template of tanks"""

    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def print_info(self):
        print(f'{self.model} имеет броню {self.armor}мм, {self.health} ед. здоровья и урон в {self.damage} единиц')

    def health_down(self, damage):
        self.health -= damage
        print(f'{self.model}:')
        print(f'Командир, по нам попали. Очков здоровья - {self.health}')

    def shot(self, name):
        if name.health <= 0:
            self.health = 0
            print(f'Экипаж танка {name.model} уничтожен.')
        else:
            name.health_down(self.damage)
            print(f'{self.model}:')
            print(f'Попали! У противника {name.model} осталось {name.health} единиц здоровья')


class SuperTank(Tank):
    def __init__(self, model, armor, min_damage, max_damage, health):
        super().__init__(model, armor, min_damage, max_damage, health)

    def health_down(self, damage):
        super().health_down(damage / 10)

tank_1 = Tank('T-34', 90, 20, 50, 100)
tank_2 = Tank('Tiger', 100, 20, 50, 120)
s = SuperTank('Super', 100, 20, 50, 100)


tank_1.print_info()
tank_2.print_info()
s.print_info()

tank_1.shot(s)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)

# class A:
#     def f(self):
#         print(1)
#
#
# class B(A):
#     pass
#
#
# a = A()
# a.f()
# b = B()
# b.f()