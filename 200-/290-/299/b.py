n, t = list(map(int, input().split()))

c = list(map(int, input().split()))
r = list(map(int, input().split()))


# 候補の番号を入れる
num = {}

if t in c:
    for i in range(n):
        if c[i] == t:
            num[i+1] = r[i] 
else:
    color = c[0]
    for i in range(n):
        if c[i] == color:
            num[i+1] = r[i] 
    
        
print(max(num, key=num.get))
        
    