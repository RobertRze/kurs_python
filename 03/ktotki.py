# #1
print ("ZADANIE 1")
my_tuple = ("kot", "dachowiec", "Lolek")
animal = []
for x in my_tuple:
    animal.append(x)
print(f"Mój {animal[0]} rasy {animal[1]} wabi się {animal[2]}")

#2
print ("ZADANIE 2")
my_tuple = (1,3,4,"kot", "kot",4)
arr = []
for x in my_tuple:
    count = my_tuple.count(x)
    if count > 1:
        arr.append(x)
arr = list(dict.fromkeys(arr))
print(arr)

#3 Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.
print("ZADANIE 3")
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