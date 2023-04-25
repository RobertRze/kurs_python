#zadania parzyste + zadanie 7

password=input('podaj hasło: ')
if len(password) < 8:
    print('za krótkie')
if password.isalpha() and password.isalnum():
    print('Potrzeba conajmniej liczbe lub litere')
if password.isalnum() and password.isdigit():
    print('lietra')
if password.islower():
    print('duża litera')
if password.isupper():
    print('mała')


"""1
num=int(input('Podaj liczbę: ')) % 3
if num==0mp
    print('podzielna')
else:
    print('nipodzielna')


#5
opinia=int(input('opinia: '))
opinia2=int(input('opinia2: '))
opinia3=int(input('opinia3: '))
avr=(opinia+opinia2+opinia3)/3
if avr >= 7:
    print('bardzo dobra')
elif  avr>=4 and avr <= 7:
    print('przecietna')
elif avr <= 4:
    print('nie warta uwagi')


"""






'''
season=input('Podaj porę roku: ').lower()
if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')

leap_year = 1
feb=(29 if leap_year else 28)
print(feb)
'''