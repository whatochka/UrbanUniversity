first = int(input("Введите число №1: "))
second = int(input("Введите число №2: "))
third = int(input("Введите число №3: "))

if first != second and second != third and first != third:
    print(0)
elif first == second and first == third:
    print(3)
else:
    print(2)
