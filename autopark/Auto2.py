from autopark import Auto1


class Electric_auto(Auto1. Auto):
    def __init__(self, mark, model, age, mileage, procent):
        super().__init__(mark, model, age, mileage)
        self.procent = procent

    def info_auto1(self):
        print(f"Этот автомобиль имеет мощность: {self.procent}%")