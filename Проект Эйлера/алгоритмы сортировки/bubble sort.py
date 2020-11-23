arr = [5, 1, 8, 3, 12, 2]
length = len(arr)
for i in range(0, length - 1):
    for j in range(0, length - i - 1):
        print("arr[j] = {}, arr[j + 1] = {}".format(arr[j], arr[j + 1]))
        if arr[j] > arr[j + 1]:
            swap = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = swap
            print(arr)

print(arr)