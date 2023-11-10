data = [{"name": "Sergey", "age": 5}, {"name": "Maxim", "age": 6}, {"name": "Ivan", "age": 7}]


def filter_data(data, age):
    return sum(map(lambda x: age < x.get("age", -1), data))


age = 6
print(filter_data(data, age))
