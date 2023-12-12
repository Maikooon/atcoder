n = int(input())
p = list(map(int, input().split()))

# 人１
p1 = p[0]

count = 0
same = 0

diff = max(p) - p1

for i in range(n):
    if p1 > p[i]:
        count += 1
    elif p1 == p[i]:
        same += 1

if diff != 0:
    print(diff+1)
elif count == n-1:
    print(0)
elif same > 0:
    print(1)
    
        
