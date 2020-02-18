scorelist=[]#創建姓名分數列表 
sumlist=[]#創建加總列表
comparelist=[]
HN="X"
LN="Y"

num=int(input("全班人數:"))#要求輸入人數
 
def gradefunction ():  #附屬程式   #對成績運算函式下定義
    for i in range(num):  
        name=input("輸入姓名:")
        grade=input("輸入成績:")
        scorelist.append(str(name))
        scorelist.append(int(grade))

    return scorelist

def sumfunction():  #附屬程式   #對加總函式下定義
    for k in range(1,num*2,2):
        sumlist.append(scorelist[k])
    return sum(sumlist) 


def comparefunction (scorelist):
    comparelist=[0, 'X', 100, 'Y']
    for g in range(1,num*2,2):
        if scorelist[g]>comparelist[0]:
            comparelist[0]=scorelist[g]
            comparelist[1]=scorelist[g-1]
              
        if scorelist[g]<comparelist[2]:
            comparelist[2]=scorelist[g]
            comparelist[3]=scorelist[g-1]
            
    return comparelist
        
scorelist = gradefunction()
comparelist = comparefunction(scorelist)
      
print('最高分是:',comparelist[1],comparelist[0],'分')
print('最低分是:',comparelist[3],comparelist[2],'分')
print("平均:",sumfunction()//num)
print(scorelist)
    