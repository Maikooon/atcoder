num = int(input())
a = list(map(int, input().split()))
total = 0

for i in range(num):
    if a[i] == a[0]:
        total += 1

if total == num:
    print("Yes")
else:
    print('No')
        