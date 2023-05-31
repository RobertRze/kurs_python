import max_val
#var = 'banannnnannnnnnnnnanananananaaaana'
#var = max_val.generator(10)
var = max_val.user_generator(10)


def main():
    score = max_val.count_str(var)

    max = 1
    for x in range(len(score)):
        max = max_val.max_of_2(score[x][1], max)

    for y in range(len(score)):
        if score[y][1] == max:
            row = y
        print(score[row][0] * max, max)

main()