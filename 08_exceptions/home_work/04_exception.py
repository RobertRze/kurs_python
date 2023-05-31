import time


def save_error_in_file(err):
    with open('log.txt', 'a') as wfile:
        wfile.write(f"\n {time.strftime(('%Y-%m-%d %H:%M:%S'))}  {err}")


def get_data():
    while True:
        try:
            numbers = input("Podaj liczby po przecinku: ")
            numbers = list(numbers.split(','))
            sum = 0
            for i in numbers:
                sum = sum + float(i)
            print(f'{sum} / {len(numbers)}')
            return float(sum) / len(numbers)
        except ValueError as err:
            save_error_in_file(f"Nieporawne dane. ERROR: {err}")
            print('Nieporawne dane. Jeszcze raz')


def main():
    print(f'średnia {get_data()}')


if __name__ == '__main__':
    main()