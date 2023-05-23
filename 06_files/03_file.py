def get_quote():
        with open("quote.txt", encoding='utf-8') as file:
            list_q = file.readlines()
            return list_q



list_q = get_quote()
#print(list_q)
for i in range(5):
    print(list_q[i])

print()