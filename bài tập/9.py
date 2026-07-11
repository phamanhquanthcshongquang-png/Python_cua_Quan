a = input("ten ho")
b = int(input("nhap chi so thang nay"))
c = int(input("nhap chi so thang nay"))
sodien = c - b
if sodien <= 60:
    print(5*sodien)
elif 60 < sodien < 161:
    print(5 * 60 + (sodien-60)*8)
else:
    print(5 * 60 + 8 * 100 + (sodien - 160))


