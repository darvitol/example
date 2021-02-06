class User:
    name = " "
    surname = ""
    age = 0
    email = ""

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def set(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def printAll(self):
        print("User: ", self.name, ", его возраст", self.age)


admin = User("админ", 'главный', 20, "admin@yandex.ru")
admin.printAll()

bob = User('Bob', "King", 45, "bob@ya.ru")
bob.printAll()
