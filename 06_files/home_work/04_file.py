import random
file = "quote.txt"
def get_quote(file):
    with open(file, encoding='utf-8') as file:
        list_q = file.readlines()
        id = random.randint(0, len(list_q) - 1)
        return list_q[id]

def show(list_q):
    print('*' * len(list_q))
    txt, author = list_q.strip().split("|")
    print(txt.center(len(list_q)))
    print(author.center(len(list_q)))
    print('*' * len(list_q))

def main():
    for i in range(3):
        queue = get_quote(file)
        show(queue)

main()