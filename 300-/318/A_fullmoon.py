n, m, p = list(map(int, input().split()))

count = 0
today = 0


if n > m:
    count += 1
    today += m
    while today < n:
        today += p
        if today <= n:
            count += 1
        else:
            break
                
print(count)      