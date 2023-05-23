def czytaj_plik():
    with open('pan_tadzio.txt', encoding='UTF-8') as fopen:
        content_list = fopen.read()

    return content_list


def wyswietlaj_liste(lista):
    print(lista)


# -----
def main():
    ksiazka_lista = czytaj_plik()
    wyswietlaj_liste(ksiazka_lista)

main()