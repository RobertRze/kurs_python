import os
import open_file

def write_to_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write('*****')

def main():
    file_name = input("Podaj nazwę pliku: ")
    if open_file.file_exist(file_name) is False:
        write_to_file(file_name)
        print('plik dodany')
    else:
        print('PLik istnieje!')

main()