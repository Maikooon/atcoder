n = int(input())

count = 'AGC'

# 正常にカウントされる
if n < 42:
    n = str(n)
    count += n.zfill(3)
    
    
# 一つ多くカウントされる
else:
    n += 1
    n = str(n)
    count += n.zfill(3)
    
print(count)