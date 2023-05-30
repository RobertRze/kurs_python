def calculate_bmi(masa, wzrost):
#        masa = float(masa.replace(",", "."))
    bmi = masa / (wzrost / 100) ** 2
#    except AttributeError:

#    print('Your BMI is:', round(bmi, 2))
    if bmi <= 18.5:
        return 'niedowaga'
    elif bmi > 18.5 and bmi <= 24.9:
        return 'waga_normalna'
    elif bmi >= 25 and bmi < 30:
        return 'nadwaga'
    elif bmi >= 30:
        return 'otyłosc'

def main():
    masa =input('Ile ważysz: ')
    wzrost = float(input('Jaki masz wzrost (cm): '))
    print(calculate_bmi(masa, wzrost))

if __name__ == '__main__':
    main()