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

    if choice_level == 'P':
        return WINERS_P
    else:
        return WINERS_T

def get_level_correct(choice_level):
    CORRECT_VALUES_T = ['k', 'n', 'p', 'j', 's']
    CORRECT_VALUES_P = ['k', 'n', 'p']
    if choice_level == 'P':
        return CORRECT_VALUES_P
    else:
        return CORRECT_VALUES_T

def get_comp_choice(CORRECT_VALUES):
    return random.choice(CORRECT_VALUES)

def get_user_choice(CORRECT_VALUES):
    while True:
        user_choice = input(f"Podaj wartości {CORRECT_VALUES}:")
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
    while True:
        comp = get_comp_choice(CORRECT_VALUES)
        user = get_user_choice(CORRECT_VALUES)
        print(f"Comp: {comp}, user {user}")
        show_result(comp, user, WINERS)
        play_again = input("Jeszcze raz t/n: ")
        if play_again.lower() == 'n':
            break
    print("dzięki")

def level():
    choice_level = input("""Podaj poziom:
        P - Prosty
        T - Trudny - """)
    start(get_level_correct(choice_level), get_level_winers(choice_level))



def main():
    choice = input("""Welcome: 
        S - Start, 
        P - Poziom 
        W - Wyjście - """)
    if choice == 'S':
        start(get_level_correct('P'), get_level_winers('P'))
    elif choice == 'W':
        print("PA!")
    elif choice == 'P':
        level()
    else:
        print("Wybór z poza zakresu")
        main()

main()