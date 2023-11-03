def to_trace(array):
    sum_trace = 0
    for i in range(len(matrix)):
        sum_trace += matrix[i][i]
    return sum_trace


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(to_trace(matrix))
