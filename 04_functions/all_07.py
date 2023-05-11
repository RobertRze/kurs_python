# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.

# pobnanie num karty - czy imput jest numerem akrty
# czy jest visa
# czy jest mastercard
# czy to american

def is_card_number(card_num):
    return card_num.isdigit()
def get_card_number():
    while True:
        card_num = input("Podaj numer karty:")
        card_num = card_num.replace(" ", "")
        card_num = card_num.replace("-", "")
        if is_card_number(card_num):
            print("Jest kartą")
            break
        else:
            print("Jeszcze raz no nie numer karty")
    return card_num
def is_visa(card_num):
    return card_num[0:1] == '4' and (len(card_num) == 16 or len(card_num) == 13)
    # if card_num[0:1] == '4' and (len(card_num) == 16 or len(card_num) == 13):
    #     return True
    # else:
    #     return False

def is_mastercard(card_num):
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)
    return len(card_num) == 16 and start_condition
    # if len(card_num) == 16 and start_condition:
    #     return True
    # else:
    #     False

def is_american(card_num):
    return (int(card_num[0:2]) == 34 or int(card_num[0:2]) == 37) and len(card_num) == 15
    # if (int(card_num[0:2]) == 34 or int(card_num[0:2]) == 37) and len(card_num) == 15:
    #     return True
    # else:
    #     False

def main():
    card_num = get_card_number()
    # print(card_num)
    if is_visa(card_num):
        print("VISA")
    elif is_mastercard(card_num):
        print("MASTERCARD")
    elif is_american(card_num):
        print("AMERICAN")
    else:
        print("unknown")

main()
