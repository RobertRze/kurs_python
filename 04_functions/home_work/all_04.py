def check_in_range(min, max, num):
    if min <= num <= max:
        return f"tak, liczba {num} znajduje się w zadanym zakresie"
    else:
        return f"nie, liczba {num} jest z poza zakresu"
min = int(input("Podaj zakres liczbowy od: "))
max = int(input("Podaj zakres liczbowy do: "))
num = int(input("Podaj liczbę: "))

print(check_in_range(min, max, num))