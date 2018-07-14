def method1():
	var = range(5)
	return var[:]

def method2():
	var = range(5)
	for v in var:
		yield v