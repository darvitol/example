class Message:
    name = ""

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print('Привет, меня зовут', self.name)


vas = Message('василий')
vas.introduce()

