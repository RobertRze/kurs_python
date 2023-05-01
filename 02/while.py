#2
print("ZADANIE 2")
secret_num = 5
input_num = int(input("Podaj liczbę od 1 do 20: "))
while input_num != secret_num:
    print("Spóbuj jeszcze raz!")
    input_num = int(input("Podaj liczbę od 1 do 20: "))
print("BRAWO!")

#1
print("ZADANIE 1")
temp = 0
while temp <= 200:
 #   print(temp)
    temp_C = round(5 / 9 * (temp - 32),2)
    print('Temp C: ', temp_C, 'Temp F: ', temp)
    temp+=20
