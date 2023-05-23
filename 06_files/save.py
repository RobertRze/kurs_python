items = ['latarka', 'woda', 'namiot', 'źdźbło', 'gąbka']

with open('example.txt', 'w', encoding='UTF-8') as fopen:
    fopen.write("\n".join(items))