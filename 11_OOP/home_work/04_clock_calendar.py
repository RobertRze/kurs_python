"""4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza. Zaimplementuj dziedziczenie wielokrotne.
Nasz zegaro-kalendarza powinen móc podawać aktualną datę oraz wyświetlać ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak,
aby zegaro-kalendarz zawierał datę, godzinę oraz widok dni ułożonych tygodniowo. Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia.
Utwórz obiekty, które będą przekazywać różne strefy czasowe i wyświetlać dzięki temu inne czasy zegara."""
import datetime, calendar, time

class Clock:
    def get_time(self):
        time_now = datetime.datetime()
        return time_now.hour, time_now.minute

class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_today(self):
        today = datetime.date.today()
        print('Aktualna data', today)

    def days_in_month(self):
        days_in_month = calendar.monthrange(self.year,self.month)
        return 'Liczba dni w {} to {}'.format(days_in_month[0], days_in_month[1])

#Calendar.get_today()
time_now = Clock()
print(time_now.get_time())
luty = Calendar(2023, 2)
# print(luty.month, luty.year)
luty.get_today()
print(luty.days_in_month())
