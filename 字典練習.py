dic={'Monday':1,'Tuesday':2,'Wednesday':3}

dic['Thursday']=4

print(dic['Tuesday'])

for i,j in dic.items():
    print(i,'是',j)
    
dic.pop('Wednesday')

for g,s in dic.items():
    print(g,'是',s)
