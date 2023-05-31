import menu, random

def fill_word():
    word_list = menu.select_category().split(",")
    word = word_list[random.randint(0, len(word_list) - 1)].strip()
    word_size = len(word)
    mask_word = len(word) * '-'
    print(mask_word)
    mask_word = list(mask_word)
    i = 0
    while mask_word.count('-') > 0 and i < 10:
        tries_number = 10 - i
        menu.check_letter(mask_word, word, tries_number)
        print(menu.show_word(mask_word))
        if mask_word.count('-') > 0:
            guest_word_result = menu.guess_word(mask_word, word, tries_number)
            mask_word = guest_word_result[0]
            i = 10 - guest_word_result[1]
            print(menu.show_word(mask_word))
            i += 1
    return menu.show_word(mask_word), word