def dec_bin(n):
    b = []
    while n > 0:
        b.append(str(n % 2))
        n //= 2
    return ''.join(reversed(b))


if __name__ == '__main__':
    n: int = int(input("Convert to binary (Enter a decimal number: "))
    print("Answer: " + dec_bin(n))
