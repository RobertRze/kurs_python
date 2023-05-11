num_list = [6,7,5]
def maximum_of(num_list):
    if num_list[1] < num_list[0] > num_list[2]:
        return num_list[0]
    elif num_list[0] < num_list[1] > num_list[2]:
        return num_list[1]
    elif num_list[0] < num_list[2] > num_list[1]:
        return num_list[2]

print(maximum_of(num_list))