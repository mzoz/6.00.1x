# 24-7-2018


# iterative
def gcd_iter(a, b):
    while b:
        a, b = b, a%b
    return a


# recursive
def gcd_rec(a, b):
    if not b:
        return a
    return gcd(b, a%b)
