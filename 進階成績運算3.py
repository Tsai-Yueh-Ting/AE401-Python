scorelist=[]#創建姓名分數列表 
sumlist=[]#創建加總列表

num=int(input("全班人數:"))#要求輸入人數
 
def gradefunction ():  #附屬函式   #對成績運算函式下定義
    name=input("輸入姓名:")
    grade=input("輸入成績:")
    scorelist.append(str(name))
    scorelist.append(int(grade))
    sumfunction(int(grade))

def sumfunction (a):  #附屬函式   #對加總函式下定義
    sumlist.append(a)
    global S
    S=sum(sumlist) 
    
for i in range(num):  #主程式
    gradefunction()
    
H=0   #比較分數程式
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

print(scorelist)   #印出分數表      
print('最高分是:',HN,H,'分')  #印出最高分
print('最低分是:',LN,L,'分')  #印出最低分
print("平均:",S/num)  #印出平均


    