n = int(input())

total = []
for i in range(n):
    s = str(input())
    total.append(s)

for i in range(n-1, -1, -1):
    print(total[i])
    
    