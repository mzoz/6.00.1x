def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)


class Fraction():
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)

    def __add__(self, other):
        n = self.numer * other.denom + self.denom * other.numer
        d = self.denom * other.denom
        g = gcd(n, d)
        n //= g
        d //= g
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.numer * other.denom - self.denom * other.numer
        d = self.denom * other.denom
        g = gcd(n, d)
        n //= g
        d //= g
        return Fraction(n, d)


x = Fraction(1, 4)
y = Fraction(1, 6)
print(x + y)
print(x - y)
