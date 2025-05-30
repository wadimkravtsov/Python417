# Перегрузка операторов
#
# Число секунд в одном днеЖ 24 * 60 * 60 = 86400

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)  # Clock(300)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    # Блок устаревших методов
    #
    # def __isub__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #     return Clock(self.sec - other.sec)
    #
    # def __imul__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #     return Clock(self.sec * other.sec)
    #
    # def __ifloordiv__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #     return Clock(self.sec // other.sec)
    #
    # def __imod__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #     return Clock(self.sec % other.sec)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return (self.sec > other.sec)

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return (self.sec >= other.sec)

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return (self.sec < other.sec)

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return (self.sec <= other.sec)


c1 = Clock(400)
c2 = Clock(150)
print('c1:', c1.get_format_time())
print('c2:', c2.get_format_time())
c3 = c1 + c2
print('c1 + c2:', c3.get_format_time())
c3 = c1 * c2
print('c1 * c2:', c3.get_format_time())
c3 = c1 // c2
print('c1 // c2:', c3.get_format_time())
c3 = c1 % c2
print('c1 % c2:', c3.get_format_time())
c1 += c2
print('c1 += c2:', c1.get_format_time())
c1 = Clock(400)  # После каждой операции для простоты контроля возвращаем исходные данные
c2 = Clock(150)
c1 *= c2
print('c1 *= c2:', c1.get_format_time())
c1 = Clock(400)
c2 = Clock(150)
c1 //= c2
print('c1 //= c2:', c1.get_format_time())
c1 = Clock(400)
c2 = Clock(150)
c1 %= c2
print('c1 %= c2:', c1.get_format_time())

c1 = Clock(100)
c2 = Clock(150)

print('c1 > c2', c1 > c2)
print('c1 >= c2', c1 >= c2)
print('c1 < c2', c1 < c2)
print('c1 <= c2', c1 <= c2)
