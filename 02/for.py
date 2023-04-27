#4
n = int(input("Podaj liczbę nie większą niż 8: "))
if n >= 8:
    print('Liczba powinna być większa niż 8')
else:
    s = 1
    for i in range(n + 1):
        if i == 0:
            print('0 ! = 1')
        else:
            s *= i
            print(i,"! =", s)




#2
items = ["woda", "herbata", "cytryna", "miód"]
print("Zagotuj wodę")
for step in items:
    print(step)
print("Podawaj w szklance")



#3
x=0
for i in range(1,11):
    x += i
    print(x)

my_list = ["ada", "ala"]
for step in my_list:
    print(step)

for step in range(5):
    print(step)

for step in range(2,10,2):
    print(step)


list=["Ada", "Julia", "Rob"]
for step in range(3):
    print(step, ':', list[step])

txt='aasjdhlafh'
for letter in txt:
    print("-", letter)
