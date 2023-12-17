N = int(input())
S = [s for s in str(input())]

is_ture = 0

for i in range(N-2):
    if S[i] == 'A':
        if S[i+1] == 'B':
            if S[i+2] == 'C':
                print(i+1)
                is_ture += 1
                break

if is_ture == 0:
    print('-1')
        