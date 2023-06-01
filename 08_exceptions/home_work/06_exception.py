import io


def open_file(file_name, mode):
    try:
        fopen = open(file_name, mode)
        x = fopen.read()
        print(x)
    except FileNotFoundError as notfound:
        print("Plik nie istnieje", notfound)
    except FileExistsError as fileexist:
        print("Plik istnieje", fileexist)
    except io.UnsupportedOperation as erroper:
        print("Błąd odczytu", erroper)


def main():
    open_file('not_exist.txt', 'r')
    open_file('exist.txt', 'w')
    open_file('exist.txt', 'x')


if __name__ == '__main__':
    main()