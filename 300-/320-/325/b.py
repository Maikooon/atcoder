n = int(input())

people = []
time = []
data = {}
for i in range(n):
    w, x = list(map(int, input().split()))
    people.append(w)
    time.append(x)
    data[w] = x
    
people = sorted(people, reverse=True)
print(people)

total = 0

for i in range(n):
    if i == 0:
        total += people[i]
    elif i== 1:
        # 一つめの時刻との差分を計算する
        diff = data[people[i]] - data[people[i-1]]
        print(diff)
        if diff <= 8:
            total += people[i]
    elif:
        for j in range(i)
    

print(total)
