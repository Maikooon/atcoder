n = int(input())
s = list(map(str, input()))

tenki = s[n-1]

if tenki == 'o':
    print('Yes')
else:
    print('No')