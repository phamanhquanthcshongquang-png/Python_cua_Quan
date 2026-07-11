def phan_tich(n):
    if n <= 1:
        print("vui lòng nhập số lớn hơn 1")
        return
    print(f"{n} =", end="")
    i = 2
    tsnt = []
    while i * i <= n:
        while n % i == 0:
            tsnt.append(str(i))
            n //= i
        i += 1
    if n > 1:
        tsnt.append(str(n))
    print("*".join(tsnt))
n = int(input("nhập số nguyên dương:"))
phan_tich(n)


    
       
