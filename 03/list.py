


arr = [ 3, 5, 7, 2, 4, 2, 6, 2]
arr.append(4)
arr.extend([1, 2, 3])
arr.insert(1, 100)
print(arr)
arr.remove(7)
print(arr.index(100))
print(arr.count(2))
arr.pop(1)
print(arr)
arr.reverse()
print(arr)
#print(arr.count(2))


# #kopiowanie listy
# import copy
# list1 = [[1, 2], [3, 4]]
# list2 = copy.copy(list1)
# list3 = copy.deepcopy(list1)
#
# # zmiana wartości w oryginalnej liście
# list1[0][1] = 5
#
# print(list1)  # [[1, 5], [3, 4]]
# print(list2)  # [[1, 5], [3, 4]]
# print(list3)  # [[1, 2], [3, 4]]
#
# #sortowanie listy
# arr = [8,3,4]
# arr.sort()
# print(arr)
# arr2 = sorted(arr)
# print(arr2)