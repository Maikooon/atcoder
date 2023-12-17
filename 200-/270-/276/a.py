s = [s for s in input()]

tag = -1

for i in range(len(s)):
    if s[i] == 'a':
        tag = i
        
if tag == -1:
    print(-1)
else:
    print(tag+1)