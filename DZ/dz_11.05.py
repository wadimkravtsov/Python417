from math import sqrt

class Area:
    __count = 0
    @staticmethod
    def s_triangle_geron(a, b, c):
        Area.__count += 1
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def s_triangle(a, h):
        Area.__count += 1
        return((a * h) / 2)

    @staticmethod
    def s_square(a):
        Area.__count += 1
        return a * a

    @staticmethod
    def s_restangle(a, b):
        Area.__count += 1
        return a * b

    @staticmethod
    def get_count():
        return Area.__count

print(f'Площадь треугольника по формуле Герона (3, 4, 5): {Area.s_triangle_geron(3, 4, 5)}')
print(f'Площадь треугольника через основание и высоту (6, 7): {Area.s_triangle(6, 7)}')
print(f'Площадь квадрата (4): {Area.s_square(4)}')
print(f'Площадь прямоугольника (4, 5): {Area.s_restangle(4, 5)}')
print(f'Количество подсчетов площади: {Area.get_count()}')
