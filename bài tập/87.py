n = int(input())
A = []
if 1000 < n < 10 ** 6:
    while n > 0:
        a = n % 10
        n = n // 10
        A.append(a)
    print(f"chữ số lớn nhất là:{max(A)}")
else:
    print("vui lòng nhập số trong khoảng 1000 đến 10**6")
