def f(a, b):
    return a+b


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}
    k1 = set(d1.keys())
    k2 = set(d2.keys())

    for k in k1 & k2:
        v = f(d1[k], d2[k])
        inter[k] = v

    for k in k1 ^ k2:
        if k in k1:
            v = d1[k]
        else:
            v = d2[k]
        diff[k] = v

    return (inter, diff)
