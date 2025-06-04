class Auto:
    def __init__(self, mark, model, age, mileage):
        self.mark = mark
        self.model = model
        self.age = age
        self.mileage = mileage

    def info_auto(self):
        print(f"{self.mark}, {self.model}, {self.age} год, {self.mileage} км")