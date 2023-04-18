masa =input('Ile ważysz: ')
wzrost = float(input('Jaki masz wzrost (cm): '))
masa=float(masa.replace(",", "."))
bmi=masa / (wzrost/100)**2
print('Your BMI is:', round(bmi, 2))