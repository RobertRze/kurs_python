


#1
def add_books(number):
    data = {}
    for i in range(number):
        title = input("Podaj tytuł: ")
        review = input("Ocen: ")
        data[title] = review
    return data
def get_book (data):
    shelt = list(data_all.items())
    size = len(shelt)

    while True:
        book_num = int(input(f"podaj numer książki (od 1 do {size}: "))
        if book_num > size or book_num < 1:
            print("nie ma")
        else:
            break
    title, review = shelt[book_num - 1]
    print(f'Ksiązla  "{title}" ma ocene {review}')
counter = int(input("ile książek: "))
data_all = add_books(counter)
print(data_all)
get_book(data_all)




# def mood(name):
#     print(f"How are you {name}?")
# name = input("Name: ")
# mood(name)

# def my_mood(answer):
#     return answer * 2
#
# resp = input("How are you? ")
# twiced = my_mood(resp)
# print("My mood is like", twiced)
