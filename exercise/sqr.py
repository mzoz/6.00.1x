def square(x):
    return square_helper(abs(x), abs(x))


def square_helper(n, x):
    if n == 0:
        return 0
    return square_helper(n-1, x) + x


print(square(-3))
