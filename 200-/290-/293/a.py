s = [s for s in input()]

for i in range(0, len(s)//2):
    a = s[2*i]
    s[2*i] = s[2*i+1]
    s[2*i+1] = a

for i in range(len(s)):
    print(s[i], end='')
