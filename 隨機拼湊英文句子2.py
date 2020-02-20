import random
namelist=['I','He','She']
nounlist=['a teacher.','an artist.','a captain.','a dentist.','a doctor.','a journalist.','My country','My hometown','This place','Taiwan']
verblist=['am','is','are']
A1=random.randint(0,2) #產生namelist隨機參數
A2=random.randint(0,5) #產生nounlist隨機參數
if A1==0:
    print(namelist[A1],verblist[0],nounlist[A2])

else:
    print(namelist[A1],verblist[1],nounlist[A2])

adjectivelist=['very beautiful.','attractive.','ancient.','modern.','lively.' ]
A3=random.randint(6,9) #產生nounlist隨機參數
A4=random.randint(0,4) #產生adjectivelist隨機參數
print(nounlist[A3],'is',adjectivelist[A4])
