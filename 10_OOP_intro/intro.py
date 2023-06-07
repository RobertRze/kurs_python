class Student:
  university = 'New York Academy'
  def __init__(self, name, last, age):
    self.name = name
    self.last = last
    self.age = age
    self.email = name + '.' + last + 'university.com'

  def mail(self):
    return '{}.{}.nya.com'.format(self.name, self.last)

obj_anna = Student('anna', 'kowalska', 23)
print(obj_anna.email)
obj_arek = Student('arkadiusz', 'nowak', 21)
print(obj_arek.email)
print(Student.mail(obj_anna))

print('Studentka {} {}'.format(obj_anna.name.capitalize(), obj_anna.last.capitalize()))
print(obj_anna.__dict__)
print(Student.__dict__)

print(type(2.0))