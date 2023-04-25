#1
word='123456789'
num=len(word)
print(word[num//2 - 1 : num//2 +2])

#2
s1='wyraz'
s2='wydwa'
len_s1=len(s1)//2
print(s1[:len_s1]+s2+s1[len_s1:])

#3
quote="Honesty is the first chapter in the book of wisdom."
print('liczba znaków w napisie: ', len(quote))
print(quote[len(quote)-7:len(quote)-1])
print(quote[:len(quote)//2])
print(quote[len(quote)-1:])
print(quote[len(quote) // 2 : : 3])
print(quote[::2])
print(quote[::-1])

#5
txt=input('Give me text: ')
txt=txt.replace(" ", "").upper()
print('In text palindron?', txt==txt[::-1])