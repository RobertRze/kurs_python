def check_odd(num):
    if num % 2 == 0:
        return 'Liczba parzysta'
    else:
        return 'Liczba nieparzysta'
num = int(input('Podaj liczbę: '))
print(check_odd(num))