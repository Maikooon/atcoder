h, w = list(map(int, input().split()))

count = 0 

for i in range(h):
    s = [s for s in input()]
    for i in range(w):
        if s[i] == "#":
            count += 1
            
print(count)