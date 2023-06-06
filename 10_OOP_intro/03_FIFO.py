class Queue:
    def __init__(self, lst):
        self.lst = lst

    def show(self):
        print(self.lst)

    def is_empty(self):
        return len(self.lst) == 0

    def put(self, element):
        self.lst.append(element)
        print('Dodano')

    def get(self):
        return self.lst.pop(0)

def main():
    kolejka = Queue([4, 23, 3, 4])
    kolejka.show()
    print(kolejka.is_empty())
    kolejka.put(6)
    print(kolejka.get())
    kolejka.show()

if __name__ == '__main__':
    main()