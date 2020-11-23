'''Решение работает, но оно крайне медленное
для маленьких чисел подходит, для больших - тупик

Lyoshas :)
'''


def is_prime(num):
    factors = 1
    for i in range(1, num + 1):
        if i > (num // 2):
            break;
        factors += num % i == 0

    return factors == 2


def biggest_factor(num):
    the_biggest_factor = 1
    for i in range(1, num + 1):
        if (num % i == 0) and (is_prime(i)):
            the_biggest_factor = i

    return the_biggest_factor


print(biggest_factor(65678878))