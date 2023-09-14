# first_var = 5
# second_var = 3.14
# print(first_var + second_var)
# print(first_var - second_var)
# print(first_var / second_var)
# print(first_var * second_var)
# print(first_var ** second_var)
# print(first_var // second_var)
# print(first_var % second_var)
# print(type(first_var), type(second_var))
# first_var = int(input('Введите первое число: '))
# second_var = int(input('Введите второе число: '))
# print('Сумма чисел', first_var, 'и', second_var, 'равна', first_var + second_var)
# print('Сумма чисел ' + str(first_var) + ' и ' + str(second_var) + ' равна ' + str(first_var + second_var))
# print('Сумма чисел {} и {} равна {}'.format(first_var, second_var, first_var+second_var))
# print(f'Сумма чисел {first_var} и {second_var} равна {first_var+second_var}')

# try:
#     first_var = int(input('Введите первое число: '))
#     second_var = int(input('Введите второе число: '))
#     if first_var > second_var:
#         print(f'Сумма чисел {first_var} и {second_var} равна {first_var+second_var}')
#     elif first_var < second_var:
#         print(-1)
#     else:
#         print('=')
# except ValueError:
#     print('Введите другое значение!')
# else:
#     print('Я успешно отработала!')
# finally:
#     print('пока')


def calculate ():
    print('Укажите интересующую вас операцию')
    print('* - умножение')
    print('/ - деление')
    print('+ - сложение')
    print('- - вычитаение')

    operation = input()

    if operation == '*':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) * int(num2)
        except ValueError:
            print("Неизвестные значения")
        else:
            print(res)
    elif operation == '/':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) / int(num2)
        except ValueError:
            print("Неизвестные значения")
        else:
            print(res)
    elif operation == '+':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) + int(num2)
        except ValueError:
            print("Неизвестные значения: ")
        else:
            print(res)
    elif operation == '-':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) - int(num2)
        except ValueError:
            print("Неизвестные значения: ")
        else:
            print(res)
    else:
        print('Операция неизвестна, повторите ввод')

    print(" ")

    calculate()

calculate()


# for i in range(1, 15, 3):
#     print(i)

# lst = [0, 1, 4, 5, 3, 4, 5, 5]
#
# print(len(lst))
#
# for i in range(len(lst)):
#     print(lst[i])


# def func_1(a, b):
#     return a + b
#
#
# def func_2():
#     print('hello')
#
#
# print(func_1(5, 6))
# func_2()

# def calculate():
#     operation = input('Введите операцию ')
#     if operation == '+':
#         try:
#             first_var = int(input('Введите первое число: '))
#             second_var = int(input('Введите второе число: '))
#             print(first_var + second_var)
#         except ValueError:
#             print('Введите другое значение!')
#     print()
#     calculate()
#
#
# calculate()
