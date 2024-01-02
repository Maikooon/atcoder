s = str(input())

true = 'Hello,World!'  
print(true) 

for i in range(min(len(s), len(true))):
    if s[i] != true[i]:
        print('WA')
        exit()
print('AC')


# 何でエラー出ているのか本当にわからなくてぴえん