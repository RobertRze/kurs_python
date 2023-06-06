place = [
'dom', 'szkoła', 'kościół', 'bar', 'szpital', 'kino', 'teatr']

graph = [
    [0,1,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,1,0,1,0],
    [1,0,1,0,1,0,0],
    [0,1,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,0,1,0,1,0,1]
]
for x in range(0,len(place)):
    for y in range(0,len(place)):
        if graph[x][y] == 1:
            print(f"{place[x]} ---- {place[y]}")


