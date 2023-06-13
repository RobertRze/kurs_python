class UsefulStuff:
    def __init__(self, name):
        print(name, 'użyteczne')

class Watch(UsefulStuff):
    def __init__(self, name):
        print(name, 'mierzy czas')


class Phone():
    def __init__(self, name):
        print(name, 'dzwoni')

class SmartWatch(Watch):
    def __init__(self):
        print('Wszystko robi')
        super().__init__('SmartWatch')


mug = UsefulStuff('mug')
watch = Watch('watch')
phone = Phone('phone')
sw = SmartWatch()