a, b = [s for s in input()]
c, d = [s for s in input()]


#ながさは２種類のみ
#隣接hしているときは短く、それ以外のときは長い
#アスキーコードを使って引き算をすると効果的
if ord(a) == ord(b)+1 or ord(a) == ord(b)-1 or ord(a) == ord(b)+4 or ord(a) == ord(b)-4:
    if ord(c) == ord(d)+1 or ord(c) == ord(d)-1 or ord(c) == ord(d)+4 or ord(c) == ord(d)-4:
        print("Yes")
    else:
        print("No")
else:
    if ord(c) == ord(d)+3 or ord(c) == ord(d)-3 or ord(c) == ord(d)+2 or ord(c) == ord(d)-2:
        print('Yes')
    else:
        print('No')


#部分文字列として含まれているか否かで判定も可能   


"""
図形問題かつ規則が見つからないとき
1.規則性に注目、答えは何通りになるのか
2.図形を配列とか一次元に落とす
"""