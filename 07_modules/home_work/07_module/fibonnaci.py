def return_fin(n):
    fin = [0, 1]
    for x in range(1, n):
        fin.append(int(fin[x - 1]) + int(fin[x]))
    return fin

