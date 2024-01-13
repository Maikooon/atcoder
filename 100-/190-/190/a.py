a, b, c = list(map(int, input().split()))

if a-1 >= b:
    print('Takahashi')
elif a <= b-1:
    print("Aoki")
else:
    if c == 0:
        print("Aoki")
    else:
        print("Takahashi")