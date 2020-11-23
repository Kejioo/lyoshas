def is_palindromic(num):
    num = str(num)
    first = num[0:len(num) // 2]
    second = num[len(num) // 2:][::-1]

    return first == second


x = 100
y = 100
z = 0

while x < 1000:
    y = 100
    while y < 1000:
        if is_palindromic(x * y) and (x * y) > z:
            z = x * y
        y += 1
    x += 1


print(z)