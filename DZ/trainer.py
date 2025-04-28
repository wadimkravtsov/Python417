# def pos_add(a, b):
#    return abs(a + b)
#
# x = 125
# y = -750
# print(pos_add(x,y))
from idlelib.configdialog import is_int

# def foo(a):
#    return divmod(a, -11)
#
#
# print(foo(121))

# def num_sum(a):
#     ty = type(a)
#     print(ty)
#
#
# x = [12,13,45]
# num_sum(x)


# def magic(*nams,k):
#     s = 0
#     for i in nams:
#         s += i ** 2
#     if s%k == 0:
#         print('Чудеса случаются')
#     else:
#         print('Чудеса не случаются')
#
#
# magic(5,4,3,1, k = 8)

# def avg_5(a,b,c,d):
#     sr = round((a + b + c + d)/4, 5)
#     print(sr)
# avg_5(7.534,11,2,4)

#
# print(max(55,6,7))

# def dislike_6(a):
#     if (type(a) is float or type(a) is int) and a == 6.0:
#         return 'Только не 6!'
#     return True
#
# print(dislike_6(6.0))

# lst = [1,2,3,4,5,6,19,38]
# print(lst[::-1])

# lst = [157,2,3,4,5,6,779]
# end = lst.pop()
# lst.insert(0,end)
# beg = lst.pop(1)
# lst.append(beg)
# print(lst)

# def magic(*args):
#     s = []
#     for i in args:
#         s.append(i)
#     print(s)
# magic(9,6,'error',8,9,True,34,67,)

# =================Списки=================

# def list_sort(lst):  #  Сортировка списка по модулю
#     list.sort(lst, key = lambda x: abs(x))
#     print(lst)
#
#
# lst = [3,5,-4,-2,6,-12,23]
# list_sort(lst)
# print(list_sort([2,6,4,8,2]))

# import random # Список из заданного количества случайных чисел и его параметры:
#
# lst = [random.randint(0, 50) for i in range(5)]
# print(lst)
# print(max(lst), min(lst), sum(lst), len(lst))
# lst.remove(max(lst))
# print(lst)
# a = int(input('Забронируйте место: '))
# x = input('Введите элемент: ')
# lst.insert(a, x)
# print(lst)

# ============ Условные выражения =========

# def is_alive(health):
#     if health <= 0:
#         return  False
#     return True
#
#
# print(is_alive(23))

# def summ(num):  # проверка деления числа на 6
#     num = str(abs(num))
#     s = 0
#     for i in num:
#         s += int(i)
#     return s
#
#
# num = int(input('Введите число: '))
# if not num%2 and not summ(num)%3:
#     print('Число делится на 6')
# else:
#     print('Число не делится на 6')
# print(num%2)
# print(not summ(num)%3)
# print(summ(num))


# ========================= Циклы =====================

# letters = 'вАПаОРдОРПиКмКЕ'  # Задача - очистить строку от заглавных букв
# new = ""
# for letter in letters:
#     if letter.lower() == letter:
#         new = new + letter
# print(new)

# rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # Вывод русского алфавита в таблицу
# for position in range(11):
#     print('^' * 27)
#     for letter in rus_lower:
#         if rus_lower.index(letter) % 11 == position:
#             print('| ', letter.upper(), letter, ' |', end='')
#     print()
# print('^' * 27)

# ============================== Функции =============================

# def sum_range(start, end):  # Сумма чисел в диапазоне
#     if start == end:
#         sum = start
#     elif start < end:
#         sum = 0
#         for i in range(start, end + 1):
#             sum += i
#     else:
#         sum = 0
#         for i in range(end, start + 1):
#             sum += i
#     return sum
#
#
# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# print('Сумма чисел в диапазоне ', sum_range(a,b))


# def keys(*, a=5, b=10, c=None):
#     if c == None:
#         print(a,b)
#     else:
#         print(a,b,c)
#
#
# keys(a = 1, b = 2, c = 12)


#============================ Строки ====================
#
# c = str.format('{0} вставляются {1}{2}', 'гвозди', 'в ', 'отверстия')
# print(c)

#============================ Кортежи ===================

# s = tuple(int(input('!')) for i in range(3))  # Заполнение кортежа с клавиатуры
# print(s)


# def tpl_sort(tp):  #  Если в кортеже все элементы - целые числа, сортируем его, если - нет оставляем без изменений!
#     x = True
#     for i in tp:
#         if isinstance(i, int):
#             pass
#         else:
#             x = False
#             break
#     if x == True:
#         tp1 = sorted(tp)
#     else:
#         return tuple(tp)
#     return tuple(tp1)
#
# tp = (2,9,45,7,34,11,10,18,6)
# print(tpl_sort(tp))


# def slicer(tp, num):  #  Функция принимает на вход кортеж и случайное число.
#     sp = []           #  Если этого числа нет в кортеже - выводится пустой кортеж.
#     tp = list(tp)     #  Если есть более одного, выводится новый кортеж - срез от этого числа до второго его появления.
#     if num not in tp:  #  Если это число есть в единственном количестве - выводится срез от этого числа до конца кортежа.
#         tp = []
#         return tuple(tp)
#     else:
#         for i in range(len(tp)):
#             if tp[i] == num:
#                 sp.append(i)
#             else:
#                 pass
#         # return(sp)
#         print(sp)
#         if len(sp) > 1:
#             tp1 = tp[sp[0]:sp[1] + 1]
#             # return tp1
#         else:
#             tp1 = tp[sp[0]:]
#         return tuple(tp1)
# tp = (1,4,9,9,5,2,7,8,10,6,8,9)
# num = 5
# print(slicer(tp,num))

# tp = (5,6,34,102,37,1267,11)  #  ищем введённое число в кортеже, если есть - удаляем его из кортежа, если нет - сохраняеь кортеж.
#
#
# def del_from_tupl(num):
#     ind = tp.index(num)
#     lst = list(tp)
#     del lst[ind]
#     print(f'Удалили из кортежа {num}, получили: {tuple(lst)}')
#
#
# print(tp)
# num = int(input('Введите любой элемент:'))
# if num not in tp:
#     print(f'Нет элемента {num} в кортеже {tp}')
# else:
#     del_from_tupl(num)


students = (('Wadim', 24, 4, 'Barnaul'), ('Svetlana', 22, 4, 'Kirov'), ('Lera', 30, 3, 'Perm'))  # кортеж кортежей с данными и баллами учеников
def good_students(students): #  вычисляем средний балл и выводим список тех, у кого балл равен или выше.
    summ = 0
    good = []
    for student in students:
        summ += student[2]
    for student in students:
        if student[2] >= summ/len(students):
            good.append(student[0])
    print('Ученики ', end = '')
    for i in good:
        print(i, end = ', ')
    print(' в этом семестре хорошо учатся')

good_students(students)
# ======================================== Леция 9 от 05.04. =============================================

# d = {'name': 'kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
# d['location'] = d.pop('city')
# print(d)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# print(d)
# print({key: value for key, value in d.items()})
# print({value: key for key, value in d.items()})  # меняем местами ключ и значение
#
# print({key: value for key, value in d.items() if value <= 2})  # вывести только два первых элемента словаря
#
# print(list(d.keys()))   # преобразование в список
# print(list(d.values()))
# print(list(d.items()))
#
# a = ["one",1,2,3,4,'two',10,20,59,'three',15,36,60,170,23,'four',-20]  #  переделываем список в словарь, строки - ключи, списки из чисел - значения.
# d = dict()
# s = None
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print

# def args(*args): # функция с переменным числом параметров
#     return args
# print(args(1,'city',[6,7,8]))

# =============================== Лекция 10 от 6.04 =============================

# print((lambda x, y, z: (x + y) / z)(1,2,3))

# import random  # генерация списка случайных чисел с заданным количеством!
#
# s = [round(random.uniform(0,9), 2) for i in range(10)]
# print(s)