numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for num in numbers:
    flag = True
    for div in range(2, (num // 2) + 1):
        if num % div == 0:
            flag = False
            not_primes.append(num)
            break
    if flag and num != 1:
        primes.append(num)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
