def prime():
    seq = []
    last = 1
    while True:
        last += 1
        for i in seq:
            if last % i == 0:
                break
        else:
            seq.append(last)
            yield last


fun = prime()
for p in fun:
    if p > 20:
        break
    print(p)
