def get_data():
    while True:
        try:
            id = int(input("Podaj indeks: "))
            value = input("Podaj wartość: ")
            return id, value
        except ValueError as err:
            print('Nieprawidłowa wartość, Jeszcze raz', err)

def main():
    my_tuple = (1, 1.2, 'x', [0, 1], True)
    id, value = get_data()
    my_tuple = list(my_tuple)
    my_tuple[id] = value
    my_tuple=tuple(my_tuple)
    print(my_tuple)


if __name__ == '__main__':
    main()