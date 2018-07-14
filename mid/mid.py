def myLog(x, b):
    i = 0;
    while pow(b, i) <= x:
        i += 1
    return i-1


def getSublists(L, n):
    result = []
    i = 0
    while i+n < len(L):
        result.append(L[i:i+n])
        i += 1
    result.append(L[i:])
    return result


def dict_invert(d):
    result = {}
    for k in d:
        v = d[k]
        if v not in result:
            result[v] = []
        result[v].append(k)

    for k in result:
        result[k].sort()

    return result


def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcd(b, a%b)


def f(i):
    return i + 2


def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    L_copy = L[:]
    for i in L_copy:
        if not g(f(i)):
            L.remove(i)
    L_copy = L[:]
    L_copy.sort()
    if L_copy:
        return L_copy[-1]
    return -1


L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
