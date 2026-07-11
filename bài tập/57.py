n = int(input())
day = [1,1]
for i in range(2,n):
    so_tiep_theo = day[-1] + day[-2]
    day.append(so_tiep_theo)
print(day)
