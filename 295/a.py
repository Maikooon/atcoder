n = int(input())
w = list(map(str, input().split()))

count = 0
for i in range(n):
    if w[i] == 'and' or w[i] == 'not' or w[i] == 'that' or w[i] == 'the' or w[i] == 'you':
        print('Yes')
        break
    else:
        count += 1
        
if count == n:
    print('No')