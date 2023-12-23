a, b = list(map(int, input().split()))

round = []
for i in range(1, 11):
    round.append(i)


if (a == 1 and b == 10) or (a == 10 and b == 1):
    print("Yes")
else:
    if round.index(a) + 1 == round.index(b) or round.index(a) - 1 == round.index(b) :
        print("Yes")
    else:
        print('No') 
    
