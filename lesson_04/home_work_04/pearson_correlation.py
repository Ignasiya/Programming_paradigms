from functools import reduce
from scipy.stats import pearsonr
import numpy as np
import math


def pearson_correlation(data_1, data_2):
    def arithmetic_mean(data):
        return reduce(lambda x, y: x + y, data) / len(data)

    def standard_deviation(data):
        return math.sqrt(arithmetic_mean([x ** 2 for x in data]) - arithmetic_mean(data) ** 2)

    def mean_of_products(data1, data2):
        return sum(map(lambda x, y: x * y, data1, data2)) / len(data1)

    return (mean_of_products(data_1, data_2) - (arithmetic_mean(data_1) * arithmetic_mean(data_2))) / (
            standard_deviation(data_1) * standard_deviation(data_2))


if __name__ == '__main__':
    array_1 = np.random.randint(0, 10, 20)
    array_2 = np.random.randint(0, 10, 20)
    print(array_1, array_2, np.corrcoef(array_1, array_2), pearsonr(array_1, array_2),
          pearson_correlation(array_1, array_2), sep='\n')
