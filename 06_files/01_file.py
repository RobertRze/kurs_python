import random
def file_name():
    file = input("Podaj plik: ")
    return file

def get_quote(file):
    try:
        with open(file, encoding='utf-8') as file:
            list_q = file.readlines()
            id = random.randint(0, len(list_q) - 1)
            return list_q[id]
    except FileNotFoundError:
        print("Nie ma takiego pliku")
        return None
def show(list_q):
    print("Quote of the day is:")
    print()
    print('*' * len(list_q))
    txt, author = list_q.strip().split("|")
    print(txt.center(len(list_q)))
    print(author.center(len(list_q)))
    print('*' * len(list_q))

def main():
    file = file_name()
    queue = get_quote(file)
    if queue is not None:
        show(queue)

main()