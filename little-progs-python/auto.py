class Auto:
    model = ''
    max_speed = 0
    color = ""

    def __init__(self, model, max_speed, color):
        self.model = model
        self.max_speed = max_speed
        self.color = color
        print('Class Cars was made!')

    def printAll(self):
        print('Модель машины:', self.model)
        print('Максимальная сокрость машины:', self.max_speed)
        print('Цвет машины:', self.color)
        print('===========')


my_car = Auto('audi', 120, 'black')
my_car.printAll()

your_car = Auto ('mersedes', 150, 'white')
your_car.printAll()

