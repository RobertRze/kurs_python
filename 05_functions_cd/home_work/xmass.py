def print_segment(n, total_width):
    for size in range(1, n+1, 2):
        print((size * "*").center(total_width))

def print_tree(total_width):
    for i in range(3, total_width + 1, 2):
        print_segment(i, total_width)

total_width = input('Rozmiar: ')
print_tree(7)