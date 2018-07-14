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