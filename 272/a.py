n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    count += a[i]
    
print(count)

