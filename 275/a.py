num = int(input())
h = list(map(int, input().split()))

max = 0

for i in range(num):
    if h[i] > max:
        max = h[i]
        tag = i

print(tag+1)