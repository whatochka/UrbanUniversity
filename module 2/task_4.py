def get_matrix(n, m, value):
    matrix = list()

    for row in range(n):
        result_col = list()
        for column in range(m):
            result_col.append(value)
        matrix.append(result_col)

    return matrix


print(get_matrix(3, 3, 10))
print(get_matrix(2, 4, 123))
print(get_matrix(2, 12, 22))
