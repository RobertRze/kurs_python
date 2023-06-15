import time
def timepassed(func):
    def ge_time():
        time_start = time.time()
        func()
        time_stop = time.time()
        return time_stop - time_start
    return ge_time


@timepassed
def example_func():
    x = input('Podaj ulubone danie: ')
    print('ale to trwało')




result = example_func()
print(result)