def check_in_range(min, max, num):
    if min <= num <= max:
        return "IN"
    else:
        return "OUT"
min = int(input("Podaj zakres liczbowy od: "))
max = int(input("Podaj zakres liczbowy do: "))
num = int(input("Podaj liczbę: "))

print(check_in_range(min, max, num))