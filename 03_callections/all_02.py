tuples_to_dict = [('a', 1), ('b',2), ('c', 3)]
dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)
for k, v in dict_from_tuples.items():
    print(f"K: {k}, V: {v}")