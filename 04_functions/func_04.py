def check_odd(num):
    if num % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'
size = int(input("Podaj wielkość listy: "))
num_list=[]
num_odd=[]
num_even=[]
for i in range(size):
    num = int(input('Podaj liczbę: '))
    num_list.append(num)
for item in num_list:
    if check_odd(item) == 'EVEN':
        num_even.append(item)
    else:
        num_odd.append(item)
print(f"Liczby parzyste: {num_even}")
print(f"Liczby nieparzyste: {num_odd}")
#print(check_odd(num))