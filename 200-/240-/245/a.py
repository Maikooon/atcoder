a, b, c, d = list(map(int, input().split()))

# まず時間を比較する
if a > c:
    print('Aoki')
elif a < c:
    print('Takahashi')
else:
    if b > d:
        print('Aoki')
    elif b < d: 
        print('Takahashi')
    else:
        print('Takahashi')
    