m = 12
balance = 3329
annualInterestRate = 0.2

def payment(b, r):
	p = 10
	while not paid(b, r, p):
		p += 10
	return p


def paid(b, r, p):
	for i in range(m):
		b = (b-p) * (1+r/12)
	if b <= 0:
		return True
	return False


print("Lowest Payment: " + str(payment(balance, annualInterestRate)))
