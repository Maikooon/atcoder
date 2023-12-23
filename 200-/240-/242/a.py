a, b, c, x = list(map(int, input().split()))

prob = 0

if x <= a:
    prob = 1
elif x > b:
    prob = 0
else:
    prob = c / (b-a)
    

print(prob)
    
