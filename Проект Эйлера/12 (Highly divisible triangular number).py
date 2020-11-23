import math
def is_triangular(num):
    # формула T(n) = 1/2 * n * (n + 1)
    # n^2 + n - 2num = 0
    a = 1
    b = 1
    c = -2 * num
    disc = math.sqrt(b**2 - 4 * a * c)
    if disc - int(disc) != 0:
        return False
    return True


def find_num_of_factors(num):
    counter = 1
    for factor in range(1, num // 2 + 1):
        if num % factor == 0:
            counter += 1

    return counter


import math

# def find_numbers_of_factors(num):
#     # находим кананочное разложение числа
#     num_copy = num
#     cur_factor = 2
#     obj = {}
#     while True:
#         # if cur_factor > num_copy // 2:
#         #     break
#         if num_copy <= 1:
#             break
#         if num_copy % cur_factor == 0:
#             num_copy /= cur_factor
#             if cur_factor in obj:
#                 obj[cur_factor] += 1
#             else:
#                 obj[cur_factor] = 1
#         else:
#             cur_factor += 1
#
#     print(obj)
#     max = 0
#     for key in obj:
#         if obj[key] > max:
#             max = obj[key]
#     max += 1# учитываем 0
#     A = len(obj) * max
#     #print(max)
#     print(A)
#
#     # используем формулу комбинаторики A
#     # result = math.factorial(sum) / math.factorial((sum - len(obj)))
#     # result = str(int(result))
#     # objLen = int(len(obj))
#     # resultLen = int(len(result))
#     #
#     # result = int(result) - objLen * (resultLen - 1) * 10
#     # print(result)
#
# print(find_numbers_of_factors(10040)) мои потуги оптимизации find_num_of_factors через каноничное разложение


the_number = 1
while True:
    if is_triangular(the_number) and find_num_of_factors(the_number) > 500:
        print(the_number)
        break
    else:
        print(the_number)

    the_number += 1

# 76576500 скрипт работал 2-3 часа