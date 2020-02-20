dic={}

while True:
    print('1:加入新單字','2:查詢單字(英翻中)','3:查詢單字(中翻英)','4:測驗','5:顯示字典')
    num=int(input('輸入欲執行之代碼:'))
    
    if num==1:
        numvoc=int(input('想輸入幾個單字:'))
        for i in range(numvoc):
            vocabulary=(input('輸入英文單字:'))
            definition=(input('輸入中文定義:'))
            dic[vocabulary]=definition

    elif num==2:
        engvoc=(input('輸入欲查詢之英文單字:'))
        if engvoc not in dic:
            print('尚未定義此字')
        else:
            print('解釋為:',dic[engvoc])
    
    elif num==3:
        chivoc=(input('輸入欲查詢之中文解釋:'))
        temp=0
        for k,v in dic.items():
            if chivoc==v:
                print(k)
                temp=1
        if temp==0:
            print('尚未定義此字')
            
    elif num==4:
        for a,b in dic.items():
            print('單字',a,end="")
            guess=str(input('解釋為:'))
            if guess==b:
                print('答對了')
            else:
                print('答錯了')                   
                print('答案是',a)
            
    elif num==5:
        print(dic)