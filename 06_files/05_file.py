with open('pan_tadzio.txt', encoding='UTF-8') as fopen:
    content = fopen.read()

content_list = content.replace('.', '').replace(',', '').replace('!', '').replace("\n", ' ').split()
content_list = set(content_list)
print(content_list)

longenst_word = ''
for word in content_list:
    if len(word) > len(longenst_word):
        longenst_word = word

print(longenst_word)