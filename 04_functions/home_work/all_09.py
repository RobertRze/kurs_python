# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy,
# że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania. ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.
import datetime


def check_car_age(cars):
    for element in cars:
        print(element, ': ', cars[element])
    today = datetime.date.today()
    year = today.year
    return year - int(cars['rocznik']) >= 25


def check_car_parts(cars):
    orginal = (cars['silnik'] + cars['karoseria'] + cars['elektryka'] + cars['zawieszenie']) / 4
    return orginal >= 0.75


def main():
    cars = {'marka': 'Fort', 'model': 'Ranger', 'rocznik': '1990', 'silnik': True, 'karoseria': True, 'elektryka': False, 'zawieszenie': False}
    if check_car_age(cars) == True and check_car_parts(cars) == True:
        print(f"Gratulacje! Twój samochód {cars['marka']} może być zarejestrowany jako zabytek.")
    elif check_car_age(cars) == True and check_car_parts(cars) == False:
        print(f"Twój samochów {cars['marka']} posiada za mało oryginalnych części")
    elif check_car_age(cars) == False and check_car_parts(cars) == True:
        print(f"Twój samochód {cars['marka']} jest jeszcze zbyt młody.")
    else:
        print(f"Twój samochów {cars['marka']} jest młodym składakien")


main()