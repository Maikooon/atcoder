n, m = map(int, input().split())

total = []
for i in range(n):
    a = []
    a = list(map(str, input()))
    total.append(a)

middle = []
count = 0

for q in range(n-8):
    for p in range(m-8):
        # とりうるますの左上の座標
        # print(total[p][q])
        # print(q, p)
        
        # 9*9のますに対して検証を行う
        count = 0
        middle = []
        for i in range(9):
            cell = []
            for j in range(9):
                cell.append(total[q+i][p+j])
            middle.append(cell)
        # print(middle)
        # もし条件を満たしていたら、pqを出力
        for s in range(3):
            for t in range(3):
                if middle[s][t] == '#' and middle[s+6][t+6] == '#':
                    count += 1
        if count == 9:
            print(q+1, p+1)

# 後二つのエラーを解消すればおk