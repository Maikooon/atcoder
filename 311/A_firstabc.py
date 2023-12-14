n = int(input())

s = [s for s in str(input())]

count = ['A', 'B', 'C']


for i in range(n):
    if s[i] in count:
        count.remove(s[i])
        if count == []:
            print(i+1)
            break 
    
