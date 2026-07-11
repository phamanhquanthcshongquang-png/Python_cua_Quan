R = float(input())
x0 = float(input())
y0 = float(input())
xa = float(input())
ya = float(input())
d = ((xa - x0)**2 + (ya - y0)**2)**0.5
if R == d:
    print("diem A nam tren duong tron")
elif R < d:
    print("diem A nam ngoai duong tron")
elif R > d:
    print("diem A nam trong duong tron")