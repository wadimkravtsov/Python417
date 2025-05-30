class Student:
    def __init__(self, name):
        self.name = name
        # self.nout = self.Noutbuck

    def print_info(self):
        print(self.name, end = " => ")

    class Noutbuck:
        def __init__(self, model, maker, memory):
            self.model = model
            self.maker = maker
            self. memory = memory

        def print_comp(self):
            print(f'{self.model}, {self.maker}, {self.memory}')


st = Student('Роман')
st.print_info()
my_nout = Student.Noutbuck('ASUS', 'i7', 16)
my_nout.print_comp()
st = Student('Vladimir')
st.print_info()
my_nout.print_comp()

