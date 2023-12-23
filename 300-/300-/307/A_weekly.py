week = int(input())
a = list(map(int, input().split()))

total = 0
new_a = a

for i in range(week):
    start = i*7
    for j in range(start, start+7):
        total += a[j]
    print(total, end=" ")
    total = 0
    


    
    