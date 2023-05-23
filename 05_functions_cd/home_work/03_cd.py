# papier kamień nożce
import random



def get_level_winers(choice_level):
    WINERS_T = {
        'k': ('n', 'j'),
        'm': ('p', 'j'),
        'p': ('k', 's'),
        'j': ('p', 's'),
        's': ('n', 'k')
    }
    WINERS_P = {
        'k': 'n',
        'm': 'p',
        'p': 'k'
    }

    if choice_level == 'p':
        return WINERS_P
    else:
        return WINERS_T

def get_level_correct(choice_level):
    CORRECT_VALUES_T = ['k', 'n', 'p', 'j', 's']
    CORRECT_VALUES_P = ['k', 'n', 'p']
    if choice_level == 'p':
        return CORRECT_VALUES_P
    else:
        return CORRECT_VALUES_T

def get_comp_choice(CORRECT_VALUES):
    return random.choice(CORRECT_VALUES)

def get_user_choice(CORRECT_VALUES):
    while True:
        user_choice = input(f"Podaj wartości {CORRECT_VALUES}:").lower()
        if user_choice in CORRECT_VALUES:
            return user_choice
        else:
            print('nieprwidłowa watrość')

def show_result(comp, user, WINERS):
    if comp == user:
        print('Remis')
    elif comp in WINERS[user]:
        print('Wygrana użytkownika')
    else:
        print('Wygrywa komputer')

def start(CORRECT_VALUES, WINERS):
    play_again = 't'
    while play_again == 't':
        comp = get_comp_choice(CORRECT_VALUES)
        user = get_user_choice(CORRECT_VALUES)
        print(f"Comp: {comp}, user {user}")
        show_result(comp, user, WINERS)
        play_again = input("Jeszcze raz t/n: ").lower()
    print("dzięki")

def level():
    play_again = 't'
    while play_again == 't':
        choice_level = input("""Podaj poziom:
            P - Prosty
            T - Trudny - """).lower()
        if choice_level == 'p' or choice_level == 't':
            start(get_level_correct(choice_level), get_level_winers(choice_level))
            play_again = start(get_level_correct(choice_level), get_level_winers(choice_level))
        else:
            print("Niepoprawny wybór poziomu. Dostępne opcje: P - prosty, T - Trudny")


def main():
    choice = input("""Welcome: 
        S - Start, 
        P - Poziom 
        W - Wyjście - """).lower()
    if choice == 's':
        start(get_level_correct('p'), get_level_winers('p'))
    elif choice == 'w':
        print("PA!")
    elif choice == 'p':
        level()
    else:
        print("Wybór z poza zakresu")
        main()

main()