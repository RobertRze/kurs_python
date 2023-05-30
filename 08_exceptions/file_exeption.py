#import sys
fopen = open('my_file.txt', 'r')


try:
    x = fopen.read()
    print(x)
    x = int(x)

except Exception:
    print('Jakies error')
#    print(sys.exc_info())

finally:
    fopen.close()
    print("Zamknięcie trybi odczytu")
