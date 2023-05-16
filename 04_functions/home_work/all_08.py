
import datetime


def check_car(cars):
    for element in cars:
        print(element, ': ', cars[element])
    today = datetime.date.today()
    year = today.year
    if year - int(cars['rocznik']) < 25:
        print(f"Twój samochód {cars['marka']} jest jeszcze zbyt młody.")
    else:
        print(f"Gratulacje! Twój samochód {cars['marka']} może być zarejestrowany jako zabytek.")


def main():
    cars = {'marka': 'Fort', 'model': 'Ranger', 'rocznik': '1999'}
    check_car(cars)


main()