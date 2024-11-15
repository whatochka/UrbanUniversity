immutable_var = tuple([1, "2", True, [4], {5: 6}])
print(f"Immutable tuple: {immutable_var}")

# immutable_var[0] = 4
# Выполнение невозможно, ибо кортеж - неизменяемый тип данных.

mutable_list = [1, "2", True, [4], {5: 6}]
mutable_list.append("modified")
print(f"Mutable list: {mutable_list}")
