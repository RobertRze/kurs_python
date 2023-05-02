#4
my_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
len_list = int(len(my_list) / 3)
x = 0
for i in range(len_list):
    res_list = my_list[x:len_list+x]
    res_list.reverse()
    print(res_list)
    x = len_list + x

#2
print("ZADANIE 2")
L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}



#3
my_tuple1 = (3, 5, 3, 4, 34, 42)
my_tuple2 = (3, 5, 3, 4, 34, 42)
tuple_to_list = list(my_tuple1[ : : 2] + my_tuple2[1 : : 2])
my_set=set(tuple_to_list)
print(tuple_to_list)
print(my_set)

#1
my_tuple = (3, 5, 3, 4, 34, 42)
my_set = set(my_tuple)
print(my_set)


