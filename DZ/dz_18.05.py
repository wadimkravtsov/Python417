from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @abstractmethod
    def info_human(self):
        pass


class Student(Human):
    def __init__(self, surname, name, age, subject, group, ball):
        super().__init__(surname, name, age)
        self.subject = subject
        self.group = group
        self.ball = ball

    def info_human(self):
        print(f"{self.surname} {self.name} {self.age} {self.subject} {self.group} {self.ball}")

class Graduate(Student):
    def __init__(self, surname, name, age, subject, group, ball, topic):
        super().__init__(surname, name, age, subject, group, ball)
        self.topic = topic

    def info_human(self):
        print(f"{self.surname} {self.name} {self.age} {self.subject} {self.group} {self.ball} {self.topic}")

class Teacher(Human):
    def __init__(self, surname, name, age, profil, rating):
        super().__init__(surname, name, age)
        self.profil = profil
        self.rating = rating

    def info_human(self):
        print(f"{self.surname} {self.name} {self.age} {self.profil} {self.rating}")

print('\nСтуденты:')
st1 = Student('Батодалаев', 'Даши', 16, 'ГК', 'Web_011',5)
st2 = Student('Загидуллин', 'Линар', 32, 'РПО', 'PD_011', 5)
st3 = Student('Маркин', 'Даниил', 17, 'ГК', 'Python_011', 5)
st4 = Student('Кравцов', 'Вадим', 64, 'Python', 'Python_417', 5)
st1.info_human()
st2.info_human()
st3.info_human()
st4.info_human()

print('\nДипломники:')
dp1 = Graduate('Шугани', 'Сергей', 15, 'РПО', 'PD_011', 5, 'Защита персональных данных')
dp1.info_human()

print('\nПреподаватели:')
tr = Teacher('Козовякина', 'Елена', 28, 'JavaScript, Python', 1000)
tr1 = Teacher('Даньшин', 'Андрей', 38, 'Астрофизика', 110)
tr2 = Teacher('Башкиров', 'Алексей', 45, 'Разработка приложений', 20)
tr.info_human()
tr1.info_human()
tr2.info_human()


