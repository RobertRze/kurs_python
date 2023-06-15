import datetime, holidays

class Student:
    school = 'UAM'
    min_avg = 4.6
    def __init__(self, firstname, lastname, age, student_avg):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.student_avg = student_avg

    def email(self):
        return f'{self.lastname}.{self.firstname[0]}@{self.school.lower()}.pl'

    def sound(self, number):
        return f'go {self.school}!' * number

    def grand(self):
        if self.student_avg >= self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa stypendium')

    @classmethod
    def set_min_avg(cls, new_min_avg):
        cls.min_avg = new_min_avg

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6 or day in holidays.PL():
            return False
        else:
            return True


anna = Student('anna', 'nowak', 23, 5.5)
adam = Student('adam', 'snow', 22, 4.5)

today = datetime.datetime.today()
print(today)

print('czy będą studenty na zajęciach', Student.academic_day(today))

# print(anna.email())
# print(adam.email())
# Student.set_min_avg(4.3)
# anna.grand()
# adam.grand()
#
# anna.lastname = 'kowal'
# print(anna.lastname)
# print(anna.email())
#
# print(anna.sound(2))
#
# print(type(6))
# print(type(anna))