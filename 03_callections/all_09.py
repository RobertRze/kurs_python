i = 0
list_s_items=[]
while i < 5:
    s_item = input("Podaj przedmiot szkolny: ")
    list_s_items.append(s_item.lower())
    i += 1
#print(list_s_items)
counting_name = {}
for item in list_s_items:
    if item in counting_name:
        counting_name[item] += 1
    else:
        counting_name[item] = 1
#print(counting_name)
count = max(counting_name.values())
print(f"Najpopularniejszy przedmiot: {list(counting_name.keys()) [list(counting_name.values()).index(count)]}")
