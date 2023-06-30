def check_is_numeric(*values):
    for item in values:
        if not isinstance(item, (int, float)):
            raise ValueError(f'{item} Bok musi być numeryczny')

def rectangle(a, b):
    check_is_numeric(a, b)
# if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    #     raise ValueError('Bok musi być numeryczny')
    return a * b


def triangle(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise ValueError('Bok musi być numeryczny')
    return 0.5 * a * h

def trapeze(a, b, h):
    if check_is_numeric(a, b, h):
        return 0.5*(a + b) * h


def main():
    print(rectangle(5, 6))


if __name__ == "__main__":
    main()