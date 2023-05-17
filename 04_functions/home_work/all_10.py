# Komputer losuje wyraz z dostępnej w programie listy wyrazów.  Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# Użykownik podaje literę.
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat: “Trafione!” oraz napis ze znanymi literami.
# W przeciwnym wpadku pokaż komunikat: “Nie trafione, spróbuj jeszcze raz!”.
# Możesz ograniczyć liczbę prób do np. 10.
import random


def check_letter(mask_word, word):
    num = 0
    while num == 0:
        letter = input('Podaj literę: ')
        num = word.count(letter)
        if num > 0:
            print("Trafione!")
            return print_word(mask_word, word, letter)
        else:
            print('Nie trafione, spróbuj jeszcze raz')
            return mask_word


def print_word(mask_word, word, letter):
    i = 0
    for i in range(len(word)):
        if word[i] == letter:
            mask_word[i] = letter
    return mask_word


def show_word(mask_word):
    format_word = ''
    for i in range(len(mask_word)):
        format_word += mask_word[i]
        i += 1
    return format_word


def fill_word():
    word_list = ['krowa', 'kot', 'pies', 'kaczka']
    word = word_list[random.randint(0, len(word_list) - 1)]
    print(word)
    word_size = len(word)
    mask_word = len(word) * '-'
    print(mask_word)
    mask_word = list(mask_word)
    i = 0
    while mask_word.count('-') > 0 and i < 10:
        check_letter(mask_word, word)
        print(show_word(mask_word))
        i += 1
    return show_word(mask_word)


def main():
    count = fill_word().count('-')
    if count > 0:
        print('Przegrałeś')
    else:
        print('Wygłałeś')

main()