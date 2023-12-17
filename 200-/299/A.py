n = int(input())
s = [s for s in str(input())]

center = 0

for i in range(n):
    if s[i] == '|':
        left = i
        break
for i in range(n-1, -1, -1):
    if s[i] == '|':
        right = i
        break

for i in range(left+1, right):
    if s[i] == '*':
        center = i
if center == 0:
    print('out')
else:
    print('in')