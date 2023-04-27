#3 Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.
my_tuple = (3, 5, 3, 4, 34, 42)
num = int(input('Podaj liczbę: '))
if num in my_tuple:
    my_tuple.index(num)
    print(f"Jest {num} na krotce: ", my_tuple.index(num))
else:
    print("NIe ma na krotce")
















# numbers = [1, 2, 3, (10, 20), 4, 5]
# counter = 0
# for n in numbers:
#   if isinstance(n, tuple):
#       break
#   counter += 1
# print('Wynik:', counter)