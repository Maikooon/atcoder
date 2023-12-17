n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in range(k):
    a.remove(a[0])
    a.append(0)
    
for i in range(len(a)):
    print(a[i], end=" ")