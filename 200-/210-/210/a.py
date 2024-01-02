n, a, x, y = list(map(int, input().split()))

total = 0

if n > a:
    total = y * (n-a) + x * a
elif n <= a:
    total = x * n
    
print(total)
    