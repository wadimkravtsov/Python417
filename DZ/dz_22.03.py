from math import pi

def restangle(a, b):
    square = a * b
    return square


def triangle(a, b):
    square = (a * b)/2
    return square

def circle(a):
    square = round(a ** 2 * pi, 2)
    return square


n = int(input('Введите номер фигуры (1 - прямоугольник, 2- треугольник, 3 - круг): '))
print(n)
if n == 1:
    x,y = input('Введите через запятую длину и высоту прямоугольника: ').split(',')
    x = int(x)
    y = int(y)
    result = restangle(x, y)
    print('Площадь прямоугольника: ', result)
elif n == 2:
    x,y = input('Введите через запятую основание и высоту треугольника: ').split(',')
    x = int(x)
    y = int(y)
    result = triangle(x, y)
    print('Площадь треугольника: ', result)
elif n == 3:
    x = int(input('Введите радиус круга: '))
    result = circle(x)
    print('Площадь круга: ', result)
else:
    print('Ошибка ввода')