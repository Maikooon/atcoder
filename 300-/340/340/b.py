q = int(input())

a = []
result = []

for i in range(q):
    m, p = list(map(int, input().split()))
    if m == 1:
        a.append(p)
    else:
        result.append(a[len(a)-p])

for i in range(len(result)):
    print(result[i])



