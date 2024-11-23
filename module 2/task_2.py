num_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num_list_length = len(num_list)
index = 0

while True:
    if num_list[index] > 0:
        print(num_list[index])
        index += 1
    else:
        index += 1

    if index == num_list_length or num_list[index] < 0:
        break
