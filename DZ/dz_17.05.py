class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, persent, value):
        self.surname = surname
        self.num = num
        self.persent = persent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет {self.num} принадлежащий {self.surname} был закрыт")

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
        usd_vel = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_vel} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_vel = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_vel} {Account.suffix_eur}")

    def edit_owner(self, surnname):
        self.surname = surnname

    def add_percent(self):
        self.value += self.value * self.persent
        print("Проценты были успешно начислены.")
        self.print_balance()

    def withdrow_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято")
            self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий бвланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.persent:.0%}")
        print("_" * 20)



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










