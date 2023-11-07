def positiv_zero_negative(arr: list[int]):
    length = len(arr)
    if length == 0:
        raise ValueError("Empty list")

    result = [0, 0, 0]
    for n in arr:
        if n > 0:
            result[0] += 1
        elif n < 0:
            result[1] += 1
        else:
            result[2] += 1

    for i, k in enumerate(result):
        result[i] = k / length

    return result


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, -1, -4, -7, -2]
print(*(positiv_zero_negative(array)))