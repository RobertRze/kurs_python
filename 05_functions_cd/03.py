# papier kamień nożce
import random

WINERS = {
    'k': ('n', 'j'),
    'm': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}
CORRECT_VALUES = ['k', 'n', 'p', 'j', 's']
def get_comp_choice():
    return random.choice(CORRECT_VALUES)

def get_user_choice():
    while True:
        user_choice = input("Podaj wartości (k, n, k, j, s):")
        if user_choice in CORRECT_VALUES:
            return user_choice
        else:
            print('nieprwidłowa watrość')

def show_result(comp, user):
    if comp == user:
        print('Remis')
    elif comp in WINERS[user]:
        print('Wygrana użytkownika')
    else:
        print('Wygrywa komputer')

def main():
    while True:
        comp = get_comp_choice()
        user = get_user_choice()
        print(f"Comp: {comp}, user {user}")
        show_result(comp, user)
        play_again = input("Jeszcze raz t/n:")
        if play_again.lower() == 'n':
            break
    print("dzięki")

main()