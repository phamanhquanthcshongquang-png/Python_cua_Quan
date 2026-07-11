from decimal import *
AB, AC = map(int, input().split())
s = AB * AC / Decimal(8)
print(f"{s:.6f}")