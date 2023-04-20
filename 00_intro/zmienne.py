consumption=float(input('Podaj spalanie: '))
distance = float(input('Podaj trase: '))
gas_price= float(input('Podaj cenę: '))
price = consumption * distance/100 * gas_price
print('Koszt całkowity: ', round(price, 2))