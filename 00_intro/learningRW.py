name=input('Hej jak masz na imię: ')
print('Cześć',name)
play=input('Pobawimy się (tak/nie)? ')
if play=='nie':
    print('To pa')
else:
    print('Super')
def animals(question, animal):
    animalIn=input(question + ': ')
    if animal==animalIn:
        print('BRAWO')
    else:
        print(animal)
animals("Robi miau", "kot")
animals('Szczeka','pies')
animals('Pływa', 'ryba')
animals('MUUUUUUU', 'krowa')
animals('Ma rogi i brodę', 'koza')
print('Dziękuje super zabawa!')