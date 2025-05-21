class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, persent, value):
        self.__surname = surname
        self.__num = num
        self.__persent = persent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет {self.__num} принадлежащий {self.__surname} был закрыт")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        usd_vel = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_vel} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_vel = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_vel} {Account.suffix_eur}")

    def edit_owner(self, surnname):
        self.__surname = surnname

    def add_percent(self):
        self.__value += self.__value * self.__persent
        print("Проценты были успешно начислены.")
        self.print_balance()

    def withdrow_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снято")
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий бвланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__persent:.0%}")
        print("_" * 20)

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def persent(self):
        return self.__persent

    @persent.setter
    def persent(self, persent):
        self.__persent = persent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value



acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)

acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percent()
print()

acc.withdrow_money(3000)
print()

acc.withdrow_money(100)
print()

acc.add_money(5000)
print()

acc.withdrow_money(3000)
print()