num=input("請輸入人數:")
scorelist = []
最高分=0
最低分=100
for i in range(int(num)):
    grade=input("輸入成績:")
    scorelist.append(int(grade))
    if int(grade)>最高分:
        最高分=int(grade)
    if int(grade)<最低分:
        最低分=int(grade)
print("平均:",sum(scorelist)/int(num))
print("最低分是:",最低分)
print("最高分是:",最高分)