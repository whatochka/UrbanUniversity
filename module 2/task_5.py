def gen_key(num):
    result_field = str()

    for div_1 in range(1, 20):
        for div_2 in range(1, 20):
            result_div = div_1 + div_2
            if num % result_div == 0 and div_1 < div_2:
                result_field += str(div_1) + str(div_2)

    return result_field


def check_num(string):
    if string.isdigit():
        return True

    return False


def check_range(number):
    if 2 < number < 21:
        return True

    return False


while True:
    first_field = input("Введите число от 3 до 20 или exit для выхода: ").lower()

    if check_num(first_field):
        first_field = int(first_field)

        if check_range(first_field):
            second_field = gen_key(first_field)
            print(f"Generated pass: {second_field}\n")
        else:
            print(f"{first_field} не входит в диапазон от 3 до 20. Попробуйте еще раз.\n")

    elif first_field == "exit":
        break

    else:
        print(f"{first_field} не число. Попробуйте еще раз!\n")
