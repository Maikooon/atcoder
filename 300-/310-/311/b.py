n, d = list(map(int, input().split()))

total_array = []
count = []
result = []


for i in range(d):
    count.append(0)

for i in range(n):
    if i == 0:
        total_array = list(map(str, input()))
    else:
        check = []
        check = list(map(str, input()))
        for j in range(d):
            if check[j] == total_array[j] and check[j] == 'o':
                count[j] += 1
# print(total_array)
# print(count)

# 全員空いてる日が何日連続しているのかを確認する
for i in range(d):
    vacant = 0
    while i <= d-1:
        if count[i] == n-1:
            vacant += 1
        else:
            break
        i += 1
    # print(vacant)
    result.append(vacant)

print(max(result))
