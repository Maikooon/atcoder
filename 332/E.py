

N, D = list(map(int, input().split()))
w = list(map(int, input().split()))

total = 0
bun = 0

for i in range(N):
    total += w[i]
    
ave = total / D

# 平均から容量が離れる量が最小になればいい
for i in range(N):
    dif = abs(int(w[i]) - ave)
    if dif < bun:
        bun = dif
        
        
        
for i in range(D):
    dif = abs(int(w[i]) - ave)
    bun += dif ** 2
    
v = bun / D
print(ave)
print(v)

