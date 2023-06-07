class Orchid:
    flowers_kindom = 'Łąka'
    def __init__(self, color, flowering_time, species):
        self.color = color
        self.flowering_time = flowering_time
        self.species = species

    def get_flowering_time(self):
        if self.flowering_time == 'zima':
            return '{} to zły czas dla {}'.format(self.flowering_time, self.species)
        elif self.flowering_time == 'wiosna':
            return '{} to dobry czas dla {}'.format(self.flowering_time, self.species)
        elif self.flowering_time == 'lato':
            return '{} to dobry czas dla {} jak pada deszcz'.format(self.flowering_time, self.species)
        elif self.flowering_time == 'jesień':
            return '{} to średni czas dla {}'.format(self.flowering_time, self.species)
        else:
            return 'Nie ma takiej pory'


def main():
    zielona = Orchid('czerwona', 'zima', 'red')
    czerwona = Orchid('zielona', 'koko', 'green')
    zolta = Orchid('żółta', 'lato', 'yellow')
    niebieska = Orchid('niebieska', 'jesień', 'blue')
    print(zielona.color)
    print(Orchid.get_flowering_time(zielona))
    print(Orchid.get_flowering_time(czerwona))
    print(Orchid.get_flowering_time(zolta))
    print(Orchid.get_flowering_time(niebieska))


if __name__ == '__main__':
    main()