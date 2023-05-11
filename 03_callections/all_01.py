lists_to_dict = [['a', 1], ['b',2], ['c', 3]]
lists_to_dict = dict (lists_to_dict)
print(lists_to_dict)
for k, v in lists_to_dict.items():
    print(k, v)