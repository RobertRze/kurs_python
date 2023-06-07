import csv


class Mammals:
    def __init__(self, name, mammary_glands, hairs, warm_blooded, environment):
        self.name = name
        self.mammary_glands = mammary_glands
        self.hairs = hairs
        self.warm_blooded = warm_blooded
        self.environment = environment

    def check_mammal(self):
        return "Czy {} jest ssakiem?: {}".format(self.name, True if self.mammary_glands and self.warm_blooded and self.hairs else False)


def change_to_bool(x):
    if x == 'False':
        return False
    else:
        return True

def get_animals():
    try:
        with open('animals.csv', 'r', encoding='utf-8') as rfile:
            animals = csv.reader(rfile, delimiter=',')
            for animal in animals:
                x = animal[0]
                x = Mammals(animal[0], change_to_bool(animal[1]), change_to_bool(animal[2]), change_to_bool(animal[3]), animal[4])
                print(Mammals.check_mammal(x))
    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)



def main():
    get_animals()


if __name__ == '__main__':
    main()


# slon = Mammals('słoń', False, True, True, 'ląd')
# delfin = Mammals('delfin', True, False, True, 'woda')
# kon = Mammals('koń', True, True, True, 'ląd')
# bocian = Mammals('bocian', False, False, False, 'powietrze')
# print(słon.environment)
# print(Mammals.check_mammal(slon))
# print(Mammals.check_mammal(delfin))

# print('Czy {} jest ssakiem?: '.format(słon.name),  Mammals.check_mammal(słon))
