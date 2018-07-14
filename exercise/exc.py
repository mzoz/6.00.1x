try:
	#raise ZeroDivisionError("except raised within try clause")
	a = b
	c = 1/0
except NameError:
	print("handling NameError...")
	#raise ZeroDivisionError("except raised within except handler")
except ZeroDivisionError as ex:
	print("handling ZeroDivisionError...")