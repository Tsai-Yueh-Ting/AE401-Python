import random
ans=random.randint(0,20)
guess=input('請輸入數字0~20:')
N=int(guess)
if N>20 or N<0:
    print("超出題目的範圍")
elif N>ans:
    print("猜小一點")
elif N<ans:
    print("猜大一點")
else:
    print("恭喜答對")