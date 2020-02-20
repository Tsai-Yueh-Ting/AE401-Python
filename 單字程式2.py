dic={}
dic2={}

def function1():
    global dic
    global dic2
    numvoc=int(input('想輸入幾個單字:'))
    for i in range(numvoc):
        vocabulary=str(input('輸入英文單字:'))
        definition=str(input('輸入中文定義:'))
        dic[vocabulary]=definition
        dic2[definition]=vocabulary

def function2():
    global dic
    engvoc=str(input('輸入欲查詢之英文單字:'))
    print('解釋為:',dic[engvoc])
    
def function3():
    global dic2
    chivoc=str(input('輸入欲查詢之中文解釋:'))
    print('單字為:',dic2[chivoc])
    
def function4():
    global dic
    print(dic)

while True:
    print('1:加入新單字','2:查詢單字(英翻中)','3:查詢單字(中翻英)','4:顯示字典')
    num=int(input('輸入欲執行之代碼:'))
    
    if num==1:
        function1()

    elif num==2:
        function2()
        
    elif num==3:
        function3()
        
    elif num==4:
        function4()
        
