#Stwórz moduł, który zawiera funkcję implementujący wzór na deltę. W nowym pliku wykorzystaj moduł.
import delta

def main():
    while True:
        try:
            a = float(input("Podaj a: "))
            b = float(input("Podaj b: "))
            c = float(input("Podaj c: "))
            break
        except:
            print("Jeszcze raz")

    delta = delta.calculate_delta(a, b, c)
    print(f'Wyliczona delta {delta}')


if __name__ == "__main__":
    main()