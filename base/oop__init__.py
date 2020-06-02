class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_name(self):
        print(self.name)
    def say_name(self):
        print(self.age)


class Cdog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)

dd = Cdog('ss',9)

dd.say_name()