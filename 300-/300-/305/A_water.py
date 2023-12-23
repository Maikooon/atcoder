n = int(input())

diff = n % 5
loc = 0

if diff == 0:
    loc = n
    print(n)
elif diff == 1 or diff == 2:
    loc = n - diff
    print(n-diff)
else:
    loc = n + (5 - diff)
    print(loc)
    