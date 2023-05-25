import figure


def main():
    fig = input("""Podaj figurę:
    1 - koło
    2 - kwadrat
    3 - trojkąt: """)

    if fig == '1':
        r = int(input("POdaj promień: "))
        print(f'Pole koła: {figure.kolo(r)}')
    elif fig == '2':
        a = int(input('Podaj długość boku: '))
        print(f'Pole kwadratu: {figure.kwadrat(a)}')
    elif fig == '3':
        a = int(input('Podaj długość podstawy: '))
        h = int(input('Podaj wysokość: '))
        print(f'Pole trójkąta: {figure.trojkat(a, h)}')

if __name__ == '__main__':
    main()