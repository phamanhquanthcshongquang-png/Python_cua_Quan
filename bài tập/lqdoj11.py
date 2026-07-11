from decimal import *
getcontext().prec = 50
a, b, c, d, e, f, g = input().split()
s = (Decimal(a) + Decimal(b) - Decimal(c) * Decimal(d) / Decimal(e)) + Decimal(f) * Decimal(f) + Decimal(g).sqrt()
print(s)