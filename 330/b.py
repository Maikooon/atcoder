n, l, r = list(map(int, input().split()))

a = list(map(int, input().split()))
small = 10**9

for j in range(n):
    print(j)    
    for i in range(l, r+1):
        per_abs = abs(i-a[j])
        if small > per_abs:
            small = per_abs
            count = a[j]
    print(count)
    # if count >= l and count <= r:
    #     print(count, end=' ')
    # else:
    #     if count < r:
    #         print(l, end=' ')
    #     else:   
    #         print(r, end=' ')