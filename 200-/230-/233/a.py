x, y = list(map(int, input().split()))

count = 0

if x < y:
    diff = y - x
    count = diff // 10 
    amari = diff % 10
    if amari != 0:
        count += 1
    
else:
    count = 0

print(count)