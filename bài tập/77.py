n = int(input())
k = int(input())
t = 0
for i in range(1,n + 1):
    a = int(input())
    if a % k == 0:
        t += 1
print(f"có {t} số là bội của {k}")
