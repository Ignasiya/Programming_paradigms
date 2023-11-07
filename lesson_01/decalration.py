def positiv_zero_negative(arr: list[int]):
    length = len(arr)
    if length == 0:
        raise ValueError("Empty list")
    
    result = [0, 0, 0]
    result[0] = sum(map(lambda x: x > 0, arr))
    result[1] = sum(map(lambda x: x < 0, arr))
    result[2] = sum(map(lambda x: x == 0, arr))

    return list(map(lambda x: x / length, result))

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, -1, -4, -7, -2]
print(*(positiv_zero_negative(array)))