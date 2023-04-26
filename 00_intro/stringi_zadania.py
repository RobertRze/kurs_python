import this


#1
word='123456789'
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
print(quote.replace('wisdom', 'friendship'))

#4
title = input('Title: ')
author = input('Author last name: ')
pages = input('Number of pages: ')
print('Title letters only: ',title.isalpha())
print('Author letters only: ',author.isalpha())
print('Number of pages numeric only: ',pages.isdigit())
print('Title: ', title.capitalize(), ' Author: ', author.capitalize())
book = title + ' ' + author + ' ' + pages
print(book)
print('Number of letters: ', len(book))

#5
txt = input('Give me text: ')
txt = txt.replace(" ", "").upper()
print('In text palindron?', txt == txt[::-1])

#6
this: str = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print('NUmber of words: ', this.count('better'))
print(this.replace('*', ''))
print(this.replace('explain', 'understand', 1))
print(this.replace(' ', '-'))
print(this.split('.'))


#7
num = '123214'
txt = 'test'
print("Numero: {} texto: {}".format(num, txt))
