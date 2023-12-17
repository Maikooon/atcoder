n, p, q, r, s = list(map(int, input().split()))
a = list(map(int, input().split()))

new = []

for i in range(1, n+1):
    if i < p:
        new.append(a[i-1])
    elif i < r and i > q:
        new.append(a[i-1])
    elif i > s:
        new.append(a[i-1])
    elif i == r:
        for j in range(p-1, q):
            
            new.append(a[j])
    elif i == p:
        for j in range(r-1, s):
            new.append(a[j])

for i in range(n):
    print(new[i], end=' ')
