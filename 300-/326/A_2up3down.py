here, to = list(map(int, input().split()))

sub = to - here

if sub <= 2 and sub > 0:
    print("Yes")
elif sub >= -3 and sub < 0:
    print("Yes")
else:
    print('No')
