from abc import ABC, abstractmethod


class Vehicles(ABC):

    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def number_of_passengers(self):
        pass

    @abstractmethod
    def document(self):
        pass


class Bike(Vehicles):
    def wheels(self):
        print('--ROWER--')
        print('Mam 2 kółka')

    def number_of_passengers(self):
        print('max 2 pasażerów')

    def document(self):
        print('karta rowerowa')

class Car(Vehicles):
    def wheels(self):
        print('--AUTO--')
        print('Mam 4 kółka, jedno w zapasie')

    def number_of_passengers(self):
        print('max 8 pasażerów')

    def document(self):
        print('Prawo jazdy B')

class Bus(Vehicles):
    def wheels(self):
        print('--BUS--')
        print('Mam 4 kółka, jedno w zapasie')

    def number_of_passengers(self):
        print('max 40 pasażerów')

    def document(self):
        print('Prawo jazdy D')


class Truck(Vehicles):
    def wheels(self):
        print('--CIĘŻARÓWKA--')
        print('Mam 6 kółek, dwa w zapasie')

    def number_of_passengers(self):
        print('max 3 pasażerów + paka')


    def document(self):
        print('Prawo jazdy C')




def main():
    r = Bike('author')
    b = Bus('Autosan')
    c = Car('Audi')
    t = Truck('Tatra')
    veh = [r, b, c, t]
    for i in veh:
        i.wheels()
        i.number_of_passengers()
        i.document()

if __name__ == '__main__':
    main()