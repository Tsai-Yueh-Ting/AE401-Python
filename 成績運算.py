Math=input("數學:")
Eng=input("英文:")
M=int(Math)
E=int(Eng)
if M==100 or E==100:
    print("領獎學金")
elif M>90 and E>90:
    print("領獎學金")
else:
    print("成績太低")