N, M = list(map(int, input().split()))
s = [s for s in input()]

clean_M = M
dirty_M = 0
dirty_logo = 0
clean_logo = 0
logo = 0

for i in range(N):
    if s[i] == '0':
        dirty_M = 0
        clean_M = M
        clean_logo = logo
        dirty_logo = 0
    elif s[i] == '1':
        # もし無地で選択してあるTシャツがあれば
        if 0 < clean_M:
            clean_M -= 1
            dirty_M += 1
        else:
            if (clean_logo > 0):
                clean_logo -= 1
                dirty_logo += 1
            else:
                logo += 1
                dirty_logo += 1
    else:
        if (0 < clean_logo):
            clean_logo -= 1
            dirty_logo += 1
        else:
            logo += 1
            dirty_logo += 1
        
print(logo)
        



