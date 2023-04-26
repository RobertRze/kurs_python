masa =input('Ile ważysz: ')
wzrost = float(input('Jaki masz wzrost (cm): '))
masa=float(masa.replace(",", "."))
bmi=masa / (wzrost/100)**2
print('Your BMI is:', round(bmi, 2))
if bmi <= 18.5:
    print('niedowaga')
elif bmi > 18.5 and bmi <= 24.9:
    print('waga normalna')
elif bmi >= 25 and bmi < 30:
    print('nadwaga')
elif bmi >= 30:
    print('otyłość')