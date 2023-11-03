def multi_table(n):
    for i in range(1, 10):
        for j in range(1, n + 1):
            print(j, '*', i, '=', j * i, sep=' ', end='\t')
        print('\r')


def check_input():
    while True:
        try:
            n: int = int(input("Multiplication table of all numbers from 1 to n, enter n: "))
            if n < 1 or n > 9:
                raise Exception()
        except Exception:
            print("number from 1 to 9")
            continue
        return n


if __name__ == '__main__':
    num = check_input()
    multi_table(num)
