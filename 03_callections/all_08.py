dict_name = {'Norwegia': ['Nora', 'Alice', 'Jeny', 'Helga', 'Emma', 'Mia'],
             'Szwecja': ['Alice', 'Zofia', 'Lucia', 'Jade', 'Olivia', 'Mia'],
             'Polska': ['Zofia', 'Bożena', 'Aneta', 'Anna', 'Magdalena', 'Misia'],
             'Niemcy': ['Emilia','Zofia', 'Lucia', 'Jade', 'Olivia', 'Mia'],
             'Finlandia': ['Maria','Zofia', 'Lucia', 'Jade', 'Olivia', 'Mia'],
             'Portugalia': ['Maria','Zofia', 'Lucia', 'Jade', 'Olivia', 'Mia'],
             'Węgry': ['Maria', 'Zofia', 'Lucia', 'Jade', 'Olivia', 'Mia',]}
list_name = []
for k in dict_name:
    list_name = list_name + dict_name[k]

print(list_name)
contuntin_name={}
for name in list_name:
    if name in contuntin_name:
        contuntin_name[name] += 1
    else:
        contuntin_name[name] = 1
print(contuntin_name)
for name, counter in contuntin_name.items():
    if counter > 3:
        print("*", name, "-", counter, "countries")