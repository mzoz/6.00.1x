balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def remaining(b, ar, pr, m):
	ub = b
	p =0
	while m > 0:
		b = ub + ub * ar/12
		ub = b - b * pr
		m -= 1
	return ub

print("Remaining balance: " + 
	str(round(remaining(balance, annualInterestRate, monthlyPaymentRate, 12), 2)))