# 0 1 1 2 3 5 8 13 21
import fibonnaci

while True:
    try:
        n = int(input('Podaj liczbę całkowitą: '))
        print(fibonnaci.return_fin(n))
        break
    except:
        print("To nie liczba całkowita. Jeszcze raz")


