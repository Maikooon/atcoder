n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0

for i in range(m):
    total += a[b[i]-1]
print(total)