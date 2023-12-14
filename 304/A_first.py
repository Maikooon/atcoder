# n = int(input())

# list_dic = []
# for i in range(n):
#     list_dic.append(input().split())
    
# dic = dict(list_dic)
# for i in dic:
#     dic[i] = int(dic[i])

# min = min(dic.values()) 
# print(min)

# for k in dic.keys(, 5):
#     print(k)

N = int(input())  # N人の人数を入力

# N人の情報を格納するリスト
people = []
for _ in range(N):
    name, age = input().split()
    age = int(age)
    people.append((name, age))

# 年齢が最も小さい人を起点としてソート
min = min(people, key=lambda x: x[1])
print(min[1])

# ソートされた順番で名前を出力
for i in people:
    i+
    print(i[1])