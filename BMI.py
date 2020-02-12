身高=input("輸入身高(cm):")
體重=input("輸入體重(kg):")
T=int(身高)
W=int(體重)
BMI=W/(T/100)**2
BMI=int(BMI)
if BMI>=35:
    print("重度肥胖")
elif 30<=BMI and BMI<35:
    print("中度肥胖")
elif 27<=BMI and BMI<30:
    print("輕度肥胖")
elif  24<=BMI and BMI<27:
    print("過重")
elif 18.5<=BMI and BMI<24:
    print("正常範圍")
else:
    print("體重過輕")
    