
scorelist=[] #
num=int(input("全班人數:"))
for i in range(num):
    name=input("輸入姓名:")
    grade=input("輸入成績:")
    scorelist.append(str(name))
    scorelist.append(int(grade))
    
total=0
for j in range(1,num*2,2):
    total=total+scorelist[j]
    
H=0
L=100
HN="X"
LN="Y"
for g in range(1,num*2,2):
    if scorelist[g]>H:
        H=scorelist[g]
        HN=scorelist[g-1]
    if scorelist[g]<L:
        L=scorelist[g]
        LN=scorelist[g-1]
        
print('最高分是:',HN,H,'分')
print('最低分是:',LN,L,'分')
print("平均:",total/num)
print(scorelist)