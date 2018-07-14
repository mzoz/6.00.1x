m = 12
balance = 320000
annualInterestRate = 0.2



def payment(b, r):
	lb = round(balance/m, 2)
	ub = round(balance*(1+annualInterestRate/12)**12/12, 2)
	p = ub
	while True:
		rm = remaining(b, r, p)
		if abs(rm) <= 0.01:
			return round(p,2)
		if rm > 0:
			lb = p
		else:
			ub = p
		p = (lb+ub)/2


def remaining(b, r, p):
	for i in range(m):
		b = (b-p) * (1+r/12)
	return b


print("Lowest Payment: " + str(payment(balance, annualInterestRate)))
