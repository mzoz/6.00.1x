# use generator
def fib_gen(n):
	prev = 1
	curr = 1
	i = 2
	while True:
		i += 1
		temp = curr
		curr = curr + prev
		prev = temp
		if i == n:
			yield curr
			return

# use dictionary
def fib(n):
    d = {1: 1, 2: 1}

    def fib_helper(n, d):
        if n in d:
            return d[n]
        ans = fib_helper(n-1, d) + fib_helper(n-2, d)
        d[n] = ans
        return ans

    return fib_helper(n, d)
