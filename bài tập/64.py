n = int(input())
goc_n = n
a = 0
while n > 0:
    a = a * 10 + n % 10
    n //= 10
if a == goc_n:
    print("true")
else:
    print("false")

