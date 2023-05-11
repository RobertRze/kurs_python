num_list = [6,7,5]
def maximum_of(num_list):
    if num_list[1] < num_list[0] > num_list[2]:
        return num_list[0]
    elif num_list[0] < num_list[1] > num_list[2]:
        return num_list[1]
    elif num_list[0] < num_list[2] > num_list[1]:
        return num_list[2]

def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2
    # if val1 > val2:
    #     return val1
    # else:
    #     return val2

def max_of(a, b, c):
    tmp = max_of_two(a, b)
    return max_of_two(c, tmp)

def main():
    x, y, z = [15, 12, 1]
    print(max_of(x, y, z))

main()



print(maximum_of(num_list))