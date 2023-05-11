#5
print("ZADANIE 5: CIEPŁO ZIOMNO")
import random
r_num = random.randint(1, 100)
for i in range(5):
    u_num = int(input("Podaj liczbę: "))
    num = [u_num, r_num]
    num.sort()
    if  num[1] - num[0] == 0:
        print("PARZY!!!!")
        break
    elif num[1] - num[0] < 10:
        print("GORĄCO")
    elif num[1] - num[0] > 20:
        print("ZIMNO")
    elif num[1] - num[0] <= 20 and num[1] - num[0] >= 10 :
        print("CIEPŁO")
    else:
        print("PRZEGRAŁEŚ")



#4
print('ZADANIE 4: PAPIER, KAMIEŃ, NOŻYCE')
import random
num_round = int(input("Podaj liczbę rund: "))
win_u = 0
win_c = 0
for i in range(num_round):
    fig_u = input("Podaj igurę kamień (k) / papier (p) / nożyce (n) / koniec (q): ")
    list_fig_c = ["k", "p", "n"]
    fig_c = random.choice(("k", "p", "n"))
    if (fig_u == "k" and fig_c == "n") or (fig_u == "p" and fig_c == "k") or (fig_u == "n" and fig_c == "k"):
        print("Wybór komputera: ", fig_c)
        print("Wygrałeś")
        win_u += 1
    elif fig_u == fig_c:
        print("Wybór komputera: ", fig_c)
        print("REMIS")
    elif fig_u == 'q':
        print("Koniec gry !!!!")
        break
    else:
        print("Wybór komputera: ", fig_c)
        print("Komputer wygrał")
        win_c += 1
if win_u > win_c:
    print(f"WYGRAŁEŚ CAŁĄ GRĘ. Twój wynik {win_u} Wynik komputera {win_c}")
elif win_u == win_c:
    print(f"REMIS W CAŁEJ GRZE. Twój wynik {win_u} Wynik komputera {win_c}")
else:
    print(f"KOMPUTER WYGRAŁ CAŁĄ GRĘ. Twój wynik {win_u} Wynik komputera {win_c}")


#2
txt = input("Enter text: ")
x = 1
res_txt = ''
for i in range(len(txt)//2):
    res_txt = res_txt + txt[x]
    x = x + 2
print("Way one: ", res_txt)

print("Way two: ", txt[1::2])

#1
name = input('podaj imioną: ')

name_list = name.split(',')
for step in name_list:
    print('Hello ', step)


#3
lower_letters = 0
upper_letters = 0
digits = 0
other_chars = 0

txt = input('Enter text: ')

for i in txt:
    if i.isupper():
        upper_letters +=1
    elif i.islower():
        lower_letters +=1
    elif i.isdigit():
        digits += 1
    else: other_chars +=1

print('lower_letters: ', lower_letters)
print('upper_letters ', upper_letters)
print('digits ', digits)
print('other_chars ', other_chars)