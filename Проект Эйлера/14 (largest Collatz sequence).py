import math

def find_Collatz_sequence(num):
    n = num
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            n = int(n)
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence

maxLen = 1
maxArr = [1]
iterations = 1000000
for i in range(1, iterations):
    seq = find_Collatz_sequence(i)
    if len(seq) > maxLen:
        maxLen = len(seq)
        maxArr = seq

print(maxArr[0])
# 837799