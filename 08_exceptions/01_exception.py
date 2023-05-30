list = [13, 'alo', 'x', 2.01]
def my_func():
    for i in list:
        x = 10 / i
        print(x)

def main():
    try:
        my_func()
    except IndexError:
        print("Lista Poza zasięgiem")

    except TypeError:
        print("Nie podziele stringa")


main()
