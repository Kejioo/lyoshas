def find_square_difference(quantity):
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, quantity + 1):
        sum_of_squares += i**2
        square_of_sum += i
        if i == quantity:
            square_of_sum = square_of_sum**2

    return square_of_sum - sum_of_squares


print(find_square_difference(100))
# 25164150