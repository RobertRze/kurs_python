import os
import time
print(os.getcwd())
print(os.path.getsize("pan_tadzio.txt"))
print(time.ctime(os.path.getctime("pan_tadzio.txt")))
os.mkdir('new')
if os.path.exists('new'):
    print("Dodany")
    print(os.path.exists('new'))
    os.rmdir('new')
if not os.path.exists(('new')):
    print("już nie istnieje")

with open("plik.txt","w", encoding="utf-8") as file:
    file.write("Text")
os.mkdir("new")
os.rename("plik.txt","new\plik 2.txt")
os.remove("new\plik 2.txt")
os.rmdir('new')