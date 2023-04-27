#5
arr = [['Dorota', 'Wellman', 'dziennikarka'], ['Adam', 'Małysz', 'sportowiec'], ['Robert', 'Lewandowski', 'piłkarz'], ['Krystyna', 'Janda', 'aktorka']]
# for i in range(len(arr)):
#     print(arr[i][0], arr[i][1], "-", arr[i][2])

# for row in arr:
#     print(row[0], row[1], row[2])
#     print(" | ".join(row))

print('-----------')
for row in arr:
    for id, elem in enumerate(row):
        if id == 1:
            print(elem, end=' - ')
        else:
            print(elem, end=' ')
    print()

# arr = ["ala", "ma", "kota", "i", "psa"]
# for id in range(5):
#     if id == 2:
#         print(arr[id], end="***")
#     else:
#         print(arr[id], end="---> ")
#
# for id, word in enumerate(arr):
#     print(id, word)
#     if id == 2:
#         print(word, end="***")
#     else:
#         print(word, end="---> ")

# print("hello", end=" - ")
# print("kakaka", end="****")
# print("lalala")


'''
#1
items = ['czekan', 'raki', 'czołówka']
items.sort()
for elem in items:
    print(elem, '!')


#3 - opcja 1
arr = input('podaj listę słów rozdzieloną spracją: ')
arr = arr.split(' ')
if arr[0] == arr[-1]:
    print('OK elemty takie same')
else:
    print('NO - elementy różne')

#3 - opcja 2
arr = []
num = int(input('Ile: '))
for elem in range(num):
    item = input("Podaj element: ")
    arr.append(item)
print(arr)
if arr[0] == arr[-1]:
    print('OK elemty takie same')
else:
    print('NO - elementy różne')

'''