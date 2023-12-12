s = [s for s in str(input())]
true = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

for i in range(len(true)):
    if s[0] + s[1] + s[2] not in true:
        print("No")
        break
    else:
        print('Yes')
        break



