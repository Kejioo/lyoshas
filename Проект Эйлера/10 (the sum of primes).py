import math


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        # if i % 2 == 0 or i % 3 == 0 or i % 5 or i % 7:
        if num % i == 0:
            return False

    return True


iterations = 2000000
sum = 0

for i in range(1, iterations + 1):
    if is_prime(i):
        sum += i

print(sum)
# 142913828922