import figure

def get_user_rooms():
    while True:

        options = """Dostęne pokoje:
        1 - kwadrat
        2 - kolo
        3 - trojkat: """
        print(options)
        room_type = input('Jaki rodzaj pokoju (1,2,3)')
        if room_type == '1':
            a = float(input("POdaj długoś ściany"))
def main():
    rooms = {
        "kwadrat": [4, 5, 6],
        "kolo": [3, 4],
        "trojkat": [[3,4], [4,5]]
    }
    total = 0

    for shape, space in rooms.items():
        if shape == 'kwadrat':
            for wall in space:
                total += figure.kwadrat(wall)

        if shape == 'kolo':
            for radius in space:
                total += figure.kolo(radius)

        if shape == 'trojkat':
            for walls in space:
                a, b = walls
                total += figure.trojkat(a, b)

    print('Powierzchnia: ', total)

if __name__ == '__main__':
    main()