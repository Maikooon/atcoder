n = int(input())

dict = {}
min_len = []
min = 37

for i in range(1, n+1):
    c = int(input())
    a = list(map(int, input().split()))
    dict[i] = a

x = int(input())

# print(dict)

# 入っているかの確認を行う
for key, value in dict.items():
    if x in value:
        # print(key)
        if len(value) <= min:
            min = len(value)
            min_len.append(key)
# print(min_len)

min_len.sort()
print(len(min_len))
for i in range(len(min_len)):
    print(min_len[i], end=' ')
    
    
# できたけどエラーが出る原因がわからん
