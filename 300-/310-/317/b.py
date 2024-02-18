n = int(input())
a = list(map(int, input().split()))

start = a[0]
end = a[n-1]

a.sort()

for i in range(n-1):
    if a[i+1] != a[i] + 1:
        print(a[i]+1)
