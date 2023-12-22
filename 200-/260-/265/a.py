x, y, n = list(map(int, input().split()))

total = 0

if x < y/3:
    total = x * n
else:
    num = n // 3
    left = n % 3
    total = num * y + left * x

print(total)