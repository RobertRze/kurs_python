import random
def max_of_2(x, y):
  return x if x > y else y

def count_str(var):
    score = []
    count = 1
    for i in range(len(var) - 1):
        if var[i] == var[i + 1]:
            count += 1
        elif count >= 2:
            score.append([var[i], count])
            count = 1
    return score


def generator(len_var):
    var = ''
    while True:
        try:
            for i in range(len_var):
                var = str(random.randint(0, 9)) + var
            if count_str(var)[0][1] is not None:
                return var
        except IndexError:
            var = ''

def get_signs():
    while True:
        signs = input('Podaj 4 znaki: ')
        if len(signs) == 4:
            return signs
        else:
            print('PODAJ 4 ZNAKI!!')

def user_generator(len_var):
    signs = get_signs()
    var = ''
    while True:
        try:
            for i in range(len_var):
                var = str(random.choice(signs)) + var
            if count_str(var)[0][1] is not None:
                return var
        except IndexError:
            var = ''


