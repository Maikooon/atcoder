x = list(map(str, input()))

first = 0

if x[1] == '.':
    first = 2
if x[2] == '.':
    first = 3   

if len(x) == 5:
    if int(x[first]) < 5:
        print(x[0])
    else:
        print(int(x[0])+1)
else:
    if int(x[first]) < 5:
        print(int(x[0])*10+int(x[1]))
    else:
        print(int(x[0])*10+int(x[1])+1)
    