s = list(map(str, input()))

# 全ての英単語を格納する配列
mydict = {}
array = []

for i in range(len(s)):
    if s[i] not in array:
        array.append(s[i])
        mydict[s[i]] = 1
    else:
        mydict[s[i]] += 1

# print(mydict)
# print(max(mydict, key=mydict.get))

        
max_value = max(mydict.values())
max_keys = [key for key, value in mydict.items() if value == max_value]
# print(max_keys)
result = min(max_keys)
print(result)