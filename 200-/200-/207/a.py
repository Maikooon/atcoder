x = list(map(int, input().split()))

maxnum = max(x)
minnum = min(x)

x.remove(minnum)
total = 0

for i in range(2):
    total += x[i]

print(total)
