"""Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
 Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną."""

class Employee:
    company_name = 'Love Python Company'
    def __init__(self, position, salary, first_name, last_name, seniority, student):
        self.position = position
        self.salary = salary
        self.first_name = first_name
        self.last_name = last_name
        self.seniority = seniority
        self.student = bool(student)


    def increase(self):
        if self.seniority > 2:
            return 'Podwyżka dla {} {} sie należy'.format(self.first_name, self.last_name), 'należy się'
        else:
            return 'Podwyżka dla {} {} sie nie należy'.format(self.first_name, self.last_name), 'nie należy się'


    def tax(self):
        return 'Podatek dla {} {}: {}'.format(self.first_name, self.last_name, self.salary * 0.19), self.salary * 0.19

    def health_care_contribution(self):
        if self.student:
            rate = 0
        else:
            rate = 0.09
        return 'Składka zdrowotna dla {} {}: {}'.format(self.first_name, self.last_name, self.salary * rate), self.salary * rate


    def mail(self):
        vowels = 'aeiouy'
        fname_lname = '{}{}'.format(self.first_name, self.last_name)
        for letter in vowels:
            fname_lname = fname_lname.replace(letter, '')
        return '{}@{}.com'.format(fname_lname.lower(), self.company_name.replace(' ', '').lower())


    def get_summary(self):
        return '{} {} MAIL: {}, PODATEK: {}, SKŁADKA ZDROWOTNA: {}, PODWYŻKA: {}'.format(self.first_name, self.last_name, self.mail(), self.tax()[1], self.health_care_contribution()[1], self.increase()[1])


def main():
    jan_kowalski = Employee('kierownik', 1000, 'Jan', 'Kowalski', 2, True)
    john_test = Employee('Tester', 500, 'John', 'Test', 3, False)
    print(Employee.increase(jan_kowalski)[0])
    print(Employee.tax(jan_kowalski)[0])
    print(Employee.health_care_contribution(jan_kowalski)[0])
    print(Employee.mail(jan_kowalski))
    print((Employee.increase(john_test)[0]))
    print((Employee.get_summary(jan_kowalski)))
    print((Employee.get_summary(john_test)))


if __name__ == '__main__':
    main()
