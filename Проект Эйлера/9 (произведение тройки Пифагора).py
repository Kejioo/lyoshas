import math

found = False
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            c = int(c)
            print("a = {0}, b = {1}, c = {2}\na * b * c = {3}".format(a, b, c, a * b * c))
            found = True
            break
    if found:
        break
