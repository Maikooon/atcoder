N, S, K = list(map(int, input().split()))

total = 0
for i in range(N):
    price, num = list(map(int, input().split()))
    total += price * num

  
if (total >= S):
    print(total)
else:
    total += K
    print(total)