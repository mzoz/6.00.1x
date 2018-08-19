def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    def triangular():
        sum = 0
        i = 1
        while True:
            sum += i
            i += 1
            yield sum

    for t in triangular():
        if t == k:
            return True
        elif t > k:
            return False


print(is_triangular(5))
print(is_triangular(6))