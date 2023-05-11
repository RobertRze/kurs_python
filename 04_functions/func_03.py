
# items = input("Podaj listę liczb po przecinku: ")

def sum(item):
    suma = 0
    for i in item:
        suma += i
    print(suma)

items = [1, 2, 3, 4]
sum(items)