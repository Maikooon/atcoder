r, c = list(map(int, input().split()))

first_low = list(map(int, input().split()))
second_low = list(map(int, input().split()))    

if r == 1:
    print(first_low[c-1])
else:
    print(second_low[c-1])


