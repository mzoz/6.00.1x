def longestRun(L):
    l = 1
    i = 0
    for j in range(1, len(L)):
        if L[j] >= L[j-1]:
            l = max(l, j-i+1)
        else:
            i = j
    return l
