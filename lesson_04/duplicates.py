from collections import Counter


def duplicates(data):
    counts = Counter(data)
    return list(filter(lambda x: counts.get(x) > 1, data))


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 7, 9]
print(duplicates(arr))
