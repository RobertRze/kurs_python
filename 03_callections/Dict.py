translate = [('apple', 'jablko'), ('ball', 'pilka')]
en_pl = dict(translate)
print(en_pl)
print(en_pl['apple'])
en_pl['bee'] = 'pszczoła'
print(en_pl)
print(en_pl.keys())
print(en_pl.values())
print()

grades = {}.fromkeys(['Math','English','Art'], 3)
print(grades)
