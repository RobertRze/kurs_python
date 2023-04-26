#zadania parzyste + zadanie 7
#8
num1=int(input('enter digit_1: '))
num2=int(input('enter digit_2: '))
num3=int(input('enter digit_3: '))
if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num1 < num2 and num2 < num3:
    print(num3, num2, num1)
elif num2 > num1 and num1 > num3:
    print(num2, num1, num3)
elif num1 > num2 and num3 > num2:
    print(num1, num3, num2)
elif num2 > num3 and num3 > num1:
    print(num2, num3, num1)
elif num3 > num1 and num1 > num2:
    print(num3, num1, num2)

#6
num = int(input('Enter number from 1 to 100: '))
if num == 77:
    print('gratulacje!')
else:
    print('pudło!')

 

#4
txt = 'kjdfhasd;alkj'
if len(txt) > 5:
    print('longer than 5')
else:
    print('shorter than 5')
if txt.count('a') > 0:
    print(txt.replace('a', 'z'))



#2
num1 = int(input('Enter an integer: '))
num2 = int(input('Enter an integer: '))
if num1 + num2 > 100:
    print('Sum: ', num1 + num2)
else:
    print('Koniec')


#1
num=int(input('Podaj liczbę: ')) % 3
if num==0mp
    print('podzielna')
else:
    print('nipodzielna')


#3
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

#5
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
