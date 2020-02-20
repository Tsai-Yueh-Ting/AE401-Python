import random
namelist=['I','He','She','It']
nounlist=['a dog.','a cow.','a cat.','a fish']
verblist=['am','is']
A1=random.randint(0,3)
A2=random.randint(0,3)

if A1==0:
    print(namelist[A1],verblist[0],nounlist[A2])

else:
    print(namelist[A1],verblist[1],nounlist[A2])
