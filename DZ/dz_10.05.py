class Auto:

    def __init__(self, model, age, firm, power, color, price):
        self.__model = model
        self.__age = age
        self.__firm = firm
        self.__power = power
        self.__color = color
        self.__price = price

    def print_info(self):
        print('Данные автомобиля'. center(40,'*'))
        print(f'Название модели: {self.__model}\nГод выпуска: {self.__age}\nПроизводитель: {self.__firm}\nМощность двигателя: {self.__power}\nЦвет: {self.__color}\nЦена: {self.__price}')
        print('*'*40)

    def set_model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            print('Ведите строковое наименование!')

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print('Введите численное значение!')

    def set_firm(self, firm):
        if isinstance(firm, str):
            self.__firm = firm
        else:
            print('Ведите строковое наименование!')

    def set_power(self, power):
        if isinstance(power, str):
            self.__power = power
        else:
            print('Ведите строковое наименование!')

    def set_color(self, color):
        if isinstance(color, str):
            self.__color = color
        else:
            print('Ведите строковое наименование!')

    def set_price(self, price):
        if isinstance(price, int):
            self.__price = price
        else:
            print('Введите численное значение!')

    def get_model(self):
        return self.__model

    def get_age(self):
        return self.__age

    def get_firm(self):
        return self.__firm

    def get_power(self):
        return self.__power

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price


auto1 = Auto('X7 M50i', 2021, 'BMW', '530 л.с.', 'white', 10790000)
auto1.print_info()

auto1.set_model("Haval")
print(auto1.get_model())

auto1.set_age(2021)
print(auto1.get_age())

auto1.set_firm("China")
print(auto1.get_firm())

auto1.set_power("160 л.с.")
print(auto1.get_power())

auto1.set_color('black')
print(auto1.get_color())

auto1.set_price(2450000)
print(auto1.get_price())

auto1.print_info()





