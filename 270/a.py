a, b = list(map(int,input().split()))

ans = 0

""""
二人がとる得点の種類
・同点
・A>B
・B>A
"""
a_ans = []
b_ans = []
true = [1,2,4]

     
def calc_score(a, a_ans):
    if a == 1: 
        a_ans.append(1)
    elif a == 2:
        a_ans.append(2)
    elif a == 3:
        a_ans.append(1)
        a_ans.append(2)
    elif a == 4:
        a_ans.append(4)
    elif a == 5:
        a_ans.append(1)
        a_ans.append(4)
    elif a == 6:
        a_ans.append(2)
        a_ans.append(4)
    return a_ans


if a == b:
    ans = a
else:     
    calc_score(a, a_ans)
    calc_score(b, b_ans)
    for i in true:
        if i in a_ans or i in b_ans:
            ans += i
        # if i not in a_ans and i not in b_ans:
            
print(ans)
    


    
        