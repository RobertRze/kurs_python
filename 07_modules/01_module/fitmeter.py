import bmi

def give_advice(bmi_result):
    with open(f'{bmi_result}.txt', encoding='UTF-8') as fopen:
        content = fopen.read()
        return content

def main():
    mass = input('Ile ważysz: ')
    height = float(input('Jaki masz wzrost (cm): '))
    bmi_result = bmi.calculate_bmi(mass, height)
    print(f'Wynik: {bmi_result}')
    print(give_advice(bmi_result))


main()