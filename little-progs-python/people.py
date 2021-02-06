class People:
    name = ''
    age = 18

    def __init__(self, name, age):
        self.name= name
        self.age = age

    def printAll(self):
        print("Человека зовут", self.name, ", ему ", self.age, ' лет')


me = People('Dasha', 20)
me.printAll()

you = People('Mary', 13)
you.printAll()
