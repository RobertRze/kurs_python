def write_to_file(file, card):
    with open(f"{file}.txt", "a", encoding="utf-8") as file:
        file.write(card + '\n')

def get_card():
    with open("cards.txt", encoding='utf-8') as file:
        list_card = file.readlines()
        return list_card

def is_visa(card_num):
    return card_num[0:1] == '4' and (len(card_num) == 16 or len(card_num) == 13)


def is_mastercard(card_num):
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)
    return len(card_num) == 16 and start_condition


def is_american(card_num):
    return (int(card_num[0:2]) == 34 or int(card_num[0:2]) == 37) and len(card_num) == 15

def main():
    cards = get_card()
    # print(card_num)
    for card in cards:
        card = card.strip()
        if is_visa(card):
            write_to_file('visa', card)
        elif is_mastercard(card):
            write_to_file('mastercard', card)
        elif is_american(card):
            write_to_file('american', card)
        else:
            print("unknown")

main()



