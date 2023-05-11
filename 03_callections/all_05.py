#5
poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
poem = poem.replace(",", "").replace("\n", " ").lower()
poem = poem.split(" ")
contuntin_word = {}
#print(poem)
for word in poem:
    if word in contuntin_word:
       contuntin_word[word] += 1
    else:
        contuntin_word[word] = 1
print(contuntin_word)
for word, counter in contuntin_word.items():
    print("*", word, "-", counter)
