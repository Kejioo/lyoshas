prev2 = 0
prev1 = 1
sum = 0

while True:
    current = prev1 + prev2
    if current > 4000000:
        break
    elif current % 2 == 0:
        sum += current

    prev2 = prev1
    prev1 = current

print(sum)