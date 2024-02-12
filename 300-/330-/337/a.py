a = int(input())

count_a = 0
count_b = 0

for i in range(a):
    a, b = list(map(int, input().split()))
    count_a += a
    count_b += b


if count_a > count_b:
    print('Takahashi')
elif count_a == count_b:
    print('Draw')
else:
    print('Aoki')