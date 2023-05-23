handler = open("pan_tadzio.txt")
print(handler.readline())
handler.close()

print('-------')
with open("pan_tadzio.txt") as fo:
    print(fo.readline())

with open("pan_tadzio_1.txt", 'w') as fw:
    fw.write(('Helo2'))

with open("pan_tadzio_1.txt", 'a') as fa:
    fa.write(('\nHelo2'))