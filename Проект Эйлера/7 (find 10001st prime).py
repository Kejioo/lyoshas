import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


def find_10001st_prime():
    prime_numbers = []
    current_num = 2
    while len(prime_numbers) < 10001:
        if is_prime(current_num):
            prime_numbers.append(current_num)

        current_num += 1

    return prime_numbers[10000]


print(find_10001st_prime())