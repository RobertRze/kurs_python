import bmi

def give_advice(bmi_result):
    with open(f'{bmi_result}.txt', encoding='UTF-8') as fopen:
        content = fopen.read()
        return content

def get_user_input(message, type):
    while True:
        try:
            value = input(message)
            x = type(value)
            return x
        except ValueError:
            print("Jeszcze raz")

def get_user_data():
    while True:
        try:
            weight = float(input('Podaj swoją wagę [kg]: '))
            height = float(input('Podaj swoj wzrost [cm]: '))

            if weight > 597 or height > 280:
                raise ValueError('Nieprawdopodobne wartości')
            break
        except:
            print('Wartość nieprawidłowa, spróbuj jeszcze raz')
    return weight, height

def main():
    mass, height = get_user_data()
    # mass = get_user_input("Podaj wagę [kg]: ", int)
    # height = get_user_input('Jaki masz wzrost (cm): ', float)
    bmi_result = bmi.calculate_bmi(mass, height)
    print(f'Wynik: {bmi_result}')
    print(give_advice(bmi_result))


main()