my_string = input("Введите любые символы: ")
print(f"Количество введеных символов: {len(my_string)}")
print(f"Введеные символы в верхнем регистре: {my_string.upper()}")
print(f"Введеные символы в нижнем регистре: {my_string.lower()}")
print(f"Введеные символы без пробелов: {my_string.replace(" ", "")}")
print(f"Первый введеный символ: {my_string[0]}")
print(f"Последний введеный символ: {my_string[-1]}")
