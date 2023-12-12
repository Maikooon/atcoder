N = int(input())
S = [s for s in input()]
flag = 0

for i in range(N-1):
    if (S[i] == 'a' and S[i+1] == 'b'):
        print('Yes')
        flag = 0
        break
    elif (S[i] == 'b' and S[i+1] == 'a'):
        print('Yes')
        flag = 0
        break
    else:
        flag = 1 

if flag == 1:
    print("No")

        

