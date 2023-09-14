# def func(a=0, b=0):
#     print(f'a={a}')
#     print(f'b={b}')
#     print('-'*100)
#
#
# def func_2(a, b):
#     print(f'a={a}')
#     print(f'b={b}')
#
#
# func(b=1, a=5)
# func_2(1, 5)

# def func_3(a, b, c=0, f=True):
#     print(c)
#
#
# func_3(5, 5, 5)


# def sum(*args):
#     k = 0
#     for i in args:
#         k += i
#     print(k)
#
#
# sum(2, 3)


def func_4(a, *args, **kwargs):
    # print(a)
    # print(args)
    print(kwargs.get('text'))


# func_4(8, 2, 6, text=5, f=False)
# func_4(8, 2, 6, f=False)

# a = 5
# b = 8
# if a > b:
#     print('+')
# else:
#     print('-')
#
# print('+' if a > b else '-')
#
# c = 'Это правда' if a > b else 'Это ложь'
# print(c)


# a = 15
# b = 6
# c = '+' if a < b else None
# print(c)

# val = None

# if val is None:
#     val = 0

# val = 0 if val is None else val
# val = val or 5005
#
# print(val)




# lst = []
# for i in range(0, 101, 5):
#     lst.append(i)
# print(lst)
#
# lst_2 = [i for i in range(0, 101, 5)]
# print(lst_2)


# lst = []
# for i in range(101):
#     if i % 5 == 0:
#         lst.append(i)
# print(lst)
#
# lst_2 = [i for i in range(101) if i % 5 == 0]
# print(lst_2)
#
# lst_3 = [i ** 2 if i < 50 else i for i in range(101) if i % 5 == 0]
# print(lst_3)

# d = {i: len(i) for i in ['tetetet', 'sfsfsf', 'fssffsfs']}
# print(d)

'''
30
31

[100,1000]
'''

# lst = [i for i in range(100, 1001) if i % 30 == 0 or i % 31 == 0]
# print(lst)

# lst = list([2, 5])
# print(lst)
#
# t = tuple(lst)
# print(t)
# a = 1
# b = a
# a += 1
# print(b)


a = [[2, 2, 4], 2, 5]
b = a[:]
a[0].append(10)
print(id(b), id(a))
print(b)