n = 11
multi_table = [[''] * n] * n
x = 0
y = 0
for x in range(n):
    for y in range(n):
        multi_table[x][y] = x * y
    print(multi_table[x])