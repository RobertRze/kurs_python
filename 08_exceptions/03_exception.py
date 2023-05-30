list = [0, 1, 'strin', 2.34, [0, 1], True]

def get_user_index():
    while True:
        try:
            id = int(input("Podaj liczbę>: "))
            break
        except ValueError:
            print("Jeszcze raz")
    return id
def main():
    try:

        id = get_user_index()
        x = 1 / list[id]
        print(x)
    except ZeroDivisionError:
        print('nie dziel przez zero')

    except TypeError:
        print("Niepoprawne dane")

    except IndexError:
        print("Poza zakresem")


    except ValueError:
        print("niepoprawna wprowadzona dana")

    except Exception as e:
        print('nieznany ', e)

if __name__ == '__main__':
    main()