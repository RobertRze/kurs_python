class Canis:
    paws = 4
    ears = 2
    tail = 1

    def __init__(self):
        print("Jestem wilkowaty")

    def show_description(self):
        print('''Species of this genus are distinguished
                   by their moderate to large size, their massive,
                   well-developed skulls and dentition,
                   long legs, and comparatively short ears and tails''')
class Fox(Canis):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Lis istnieje ' + self.name

    def sound(self):
        return 'HOW HOW'

    def show_description(self):
        super().show_description()
        print('---FOX---')
        print("Opis jak dla wika - taki sam jak dla wilka tylko rudy")

lis_jan = Fox('jan')
print(lis_jan)
print(Fox.sound(lis_jan))
print(lis_jan.paws)
lis_jan.show_description()

