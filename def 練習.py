num=int(input("全班人數:"))  #要求輸入人數
gradelist=[]
scorelist=[]  #創建分數列表 
for i in range(num):  #主程式
        name=str(input("輸入姓名:"))
        grade=int(input("輸入成績:"))
        scorelist.append([name,grade])
        gradelist.append(int(grade))

def lenfunction ():
    print("長度",len(scorelist))#印出長度
    
def sortedfunction ():
    
    print("排序",sorted(scorelist,key=lambda x:x[1]))#印出排列  
    
def maxfunction ():
    
    print("最大值",max(gradelist))#印出最大值 
    
def minfunction ():
    print("最小值",min(gradelist))#印出最小值 
    
def sumfunction ():
    print("總和",sum(gradelist))#印出總和序
    
lenfunction ()
sortedfunction()
maxfunction()
minfunction()
sumfunction() 
    
    

