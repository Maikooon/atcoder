n = int(input())
s = [s for s in str(input())]

taka = 0
ao = 0
flag_t = 0
flag_a = 0

for i in range(n):
    if s[i] == 'T':
        taka += 1
        flag_t = i
    else:
        ao += 1
        flag_a = i
    if taka == ao and taka+ao == n:
        if flag_a > flag_t:
            print('T')
        else:
            print('A')

if taka < ao:
    print('A')
elif taka > ao:
    print('T')
