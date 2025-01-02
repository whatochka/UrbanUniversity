def calculate_structure_sum(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, (list, tuple, set)):
        return sum(calculate_structure_sum(item) for item in data)
    elif isinstance(data, dict):
        return sum(calculate_structure_sum(key) + calculate_structure_sum(value)
                   for key, value in data.items())
    else:
        return 0


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
