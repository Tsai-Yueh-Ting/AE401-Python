num=input("請輸入全班人數:")
N=int(num)
scorelist = []
namelist = []
最高分=0
最低分=100
for i in range(int(num)):
    name=input("學生姓名:")
    grade=input("輸入數學成績:")
    namelist.append(str(name))
    scorelist.append(int(grade))
    if int(grade)>最高分:
        最高分=int(grade)
        H=i
    if int(grade)<最低分:
        最低分=int(grade)
        L=i
print(namelist)
print(scorelist)
print("平均:",sum(scorelist)/int(num))
print("最低分是",namelist[L],':',最低分)
print("最高分是",namelist[H],':',最高分)