class Dog:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def bark(self, number):
        return print('HOW ' * number)

    def wave(self, number):
        return print('MACHU ' * number)

reksio = Dog('reksio', 'rudy', 'pudel')
max = Dog('max', 'bury', 'dog')
print(reksio.color)

reksio.wave(3)
reksio.bark(4)