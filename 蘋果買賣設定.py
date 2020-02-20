reduceapplelist=[]
pricereduceapplelist=[]

while True:
    print('1:設定  2:進貨  3:出貨  4.營業額統計  5:庫存統計')   #初始程式 
    num=int(input('輸入欲執行之代碼:'))
    
    if num==1:  #若選定"設定"功能
        applenum=int(input('有幾顆蘋果:'))
        price=int(input('一顆多少錢:'))
    
    elif num==2:  #若選定"進貨"功能
        addapple=int(input('要新進幾顆蘋果:'))
        applenum=applenum+addapple
        print('所以庫存變為',applenum,'顆')
    
    elif num==3:  #若選定"出貨"功能
        reduceapple=int(input('要出貨幾顆蘋果:'))
        applenum=applenum-reduceapple
        reduceapplelist.append(reduceapple)
        pricereduceapple=reduceapple*price
        pricereduceapplelist.append(pricereduceapple)
        print('共需要',pricereduceapple,'元')
        print('所以庫存變為',applenum,'顆')
        
    elif num==4:  #若選定"營業額統計"功能
        print('共賣出:',sum(reduceapplelist),'個')
        print(reduceapplelist)
        print('每次賺:',pricereduceapplelist)
        print('營業額統計:',sum(pricereduceapplelist))
    
    elif num==5:  #若選定"庫存統計"功能
        print('庫存為',applenum,'顆')
        
    #elif num==6: