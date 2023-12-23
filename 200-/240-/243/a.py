v, a, b, c = list(map(int, input().split()))

term = a + b + c
left = v % term

if left < a:
    print('F')
elif left == a:
    print('M')
elif left < a + b and left > a:
    print('M')
else:
    print('T')
