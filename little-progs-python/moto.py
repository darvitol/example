class Car:
    wheels = 4
    model = "Some"
    speed = 123.5


    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):
        print('Automobile', self.model, 'can be driven with speed of',
               self.speed, 'on its all', self.wheels, 'wheels')
        pass

class Moto(Car):
    engine = ''

    def getAll(self):
        super().getAll()
        print('Его двигатель:', self.engine)

    def set(self, wheels, model, speed, engine):
        self.wheels = wheels
        self.model = model
        self.speed = speed
        self.engine = engine


myCar = Car()
myCar.getAll()

yourCar = Car()
yourCar.set('4', 'tesla', 500)
yourCar.getAll()

myMoto = Moto()
myMoto.set('2', 'harley', 150, 'disel')
myMoto.getAll()
