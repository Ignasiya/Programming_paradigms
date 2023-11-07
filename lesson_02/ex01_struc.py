matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_trace = 0
for i in range(len(matrix)):
    sum_trace += matrix[i][i]

print(sum_trace)
