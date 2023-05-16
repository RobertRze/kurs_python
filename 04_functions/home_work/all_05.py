print("ZADANIE 5: CIEPŁO ZIOMNO")
import random


def hot_cold_game_result(level, random_num):
    for i in range(level):
        user_num = int(input("Podaj liczbę: "))
        num = [user_num, random_num]
        num.sort()
        if num[1] - num[0] == 0:
            return 'win'
            break
        elif num[1] - num[0] < 10:
            print("GORĄCO")
        elif num[1] - num[0] > 20:
            print("ZIMNO")
        elif num[1] - num[0] <= 20 and num[1] - num[0] >= 10 :
            print("CIEPŁO")


def hot_cold_game(level):
    random_num = random.randint(1, 100)
    one_more = 'Y'
    while one_more == 'Y':
        result = hot_cold_game_result(level, random_num)
        if result == 'win':
            print("WYGRAŁEŚ")
            one_more = input("Jeszcze raz? (Y/N), Zmień poziom (Z): ")
        else:
            print("PRZEGŁAŁEŚ")
            one_more = input("Jeszcze raz? (Y/N), Zmień poziom (Z) : ")
    return one_more

def main():
    result = 'Z'
    while result == 'Z':
        level = input("Wybierz (E-easy, M-medium, H - hard): ")
        level_dict = {'E': 12, 'M': 7, 'H': 4}
        result = hot_cold_game(level_dict[level])

main()