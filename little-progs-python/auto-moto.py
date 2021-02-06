class Auto:
    model = ''
    color = ''
    speed = 80

    def set(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def info(self):
        print('Модель:', self.model)
        print('Color:', self.color)
        print('Speed:', self.speed)
        print("=========")


class Moto (Auto):

    weight = 120

    def set(self, model, color, speed, weight):
        self.model = model
        self.color = color
        self.speed = speed
        self.weight = weight


my_moto = Moto()
my_moto.set('fox', 'black', 90, 176)
my_moto.info()
print(my_moto.weight)
