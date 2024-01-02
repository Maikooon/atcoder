a, b = list(map(int, input().split()))

if a > b:
    count = 0
else:
    count = b-a + 1
print(count)