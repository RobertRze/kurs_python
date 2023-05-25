import os
def file_exist(file_name):
    if os.path.isfile(file_name) is False:
        return False
    else:
        if os.path.getsize(file_name) == 0:
            return False
        else:
            return True

def main():
    file_exist("test.txt")


if __name__ == '__mani__':
    main()
