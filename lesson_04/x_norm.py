def norm(array):
    max_el = max(array)
    min_el = min(array)
    return list(map(lambda x: (x - min_el) / (max_el - min_el), array))
