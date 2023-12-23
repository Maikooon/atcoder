N, X = list(map(int, input().split()))
s = list(map(int, input().split()))

total = 0

for i in range(N):
    if s[i] <= X:
        total += s[i]
        
print(total)

