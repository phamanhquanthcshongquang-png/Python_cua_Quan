a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4 * a * c 
n1 = (-b + delta**0.5) / (2*a)
n2 = (-b - delta**0.5) / (2*a)
n = -b / (2 * a)
if delta > 0:
    print("phương trình có hai nghiệm phân biệt")
    print(f"x1 = {n1}")
    print(f"x2 = {n2}")
elif delta == 0:
    print(f"phương trình có nghiệm kép x1 = x2 = {n}")
else:
    print("phương trình vô nghiệm")

    