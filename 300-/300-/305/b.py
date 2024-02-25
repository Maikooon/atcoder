p, q = list(map(str, input().split()))


dist = {}
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
long = [0, 3, 1, 4, 1, 5, 9]


result = 0
# 　何番目か判断したのちに、そこまで合計する
start = alp.index(p)
end = alp.index(q)

# 順番が正しくなるようにする
if start > end:
    a = start
    start = end
    end = a
# print(start)
# print(end)


for i in range(start+1, end+1):
    # print(long[i])
    result += long[i]

print(result)
