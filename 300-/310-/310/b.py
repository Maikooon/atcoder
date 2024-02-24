n, m = list(map(int, input().split()))

all = []
tag = 0

for i in range(n):
    a = list(map(int, input().split()))
    all.append(a)

# print(all)


# 機能を列挙する関数
def func(a):
    # 機能の数
    num = a[1]
    func = []
    for i in range(2, num+2):
        func.append(a[i])
    return func


# 二つの配列を比較する関数,前者にIに相当するものを入れる
def compare(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] in b:
            count += 1
            # ここがTrueで最後まで行けば条件を満たす
    if count == len(a):
        return True
    else:
        return False

    
# 機能の量を比較する関数
# 全ての商品を比べてく
for i in range(n-1):
    a = all[i]
    for j in range(i+1, n):
        b = all[j]
        # 条件１
        if a[0] >= b[0]:
            # 条件２ 
            # 最低限の機能があるのか
            if compare(func(a), func(b)):
                # print(func(a), func(b)) 
                if a[0] > b[0] or len(func(a)) > len(func(b)):  
                    tag += 1

for i in range(n-1):
    a = all[i]
    for j in range(i+1, n):
        b = all[j]
        # 条件１
        if b[0] >= a[0]:
            # 条件２ 
            # 最低限の機能があるのか
            if compare(func(b), func(a)):
                # print(func(b), func(a)) 
                if b[0] > a[0] or len(func(b)) > len(func(a)):  
                    tag += 1
            
if tag > 0:
    print('Yes')   
else:
    print('No')       
    
# 一つだけエラーあっるけどあと一つだけkk