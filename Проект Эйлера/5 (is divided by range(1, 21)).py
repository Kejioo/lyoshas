num = 0

while True:
    num += 20
    is_divided = True

    for i in range(1, 21):
        is_divided = is_divided and num % i == 0
        if not is_divided:
            break

    if is_divided:
        break


print(num)