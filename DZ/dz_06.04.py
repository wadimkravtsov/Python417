# a,b,c = input('Введите через запятую длину, ширину и высоту параллелепипеда: ').split(',')
# a = int(a)
# b = int(b)
# c = int(c)
# s = 0  # глобальная переменная
#
#
# def square(a1, b1, c1):
#     def square1(x, y):
#         s2 = x * y
#         return s2
#     s1 = 2 * (square1(a1, b1) + square1(a1, c1) + square1(b1, c1))
#     return s1
#
#
# s = square(a, b, c)
# print('Площадь поверхности параллелограмма:',s)


# a,b,c = input('Введите через запятую длину, ширину и высоту параллелепипеда: ').split(',')
# a = int(a)
# b = int(b)
# c = int(c)
#
#
# def square(a, b, c):
#     def square1(x, y, z):
#         s = 2 * (x * y + x * z + y * z)  # s - локальная переменная
#         print(s)
#     square1(a, b, c)
#
# square(a, b, c)


a,b,c = input('Введите через запятую длину, ширину и высоту параллелепипеда: ').split(',')
a = int(a)
b = int(b)
c = int(c)


def square(a, b, c):
    def square1(x, y, z):
        nonlocal s
        s = 2 * (x * y + x * z + y * z)  # s - не локальная переменная
        # print(s)
    s = 0
    square1(a, b, c)
    return s

print(square(a, b, c))


