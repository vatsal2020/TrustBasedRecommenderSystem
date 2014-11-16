import numpy as np
rawdata=[]
rawdata1=[]
rawdata=np.genfromtxt("data\\ratings_data.txt",delimiter='',dtype=int)
s=np.shape(rawdata)
print s

noofusersperitem=np.zeros(139739)

noofitemsperuser=np.zeros(49290)

for i in range(s[0]):
    item=rawdata[i][1]
    noofusersperitem[item] = noofusersperitem[item]+1

L=np.where(noofusersperitem <= 3)
print np.shape(L)


for i in range(s[0]):
    item=rawdata[i][1]
    user=rawdata[i][0]
    if item in L[0]:
        noofitemsperuser[user]= noofitemsperuser[user]+1

U=np.where(noofitemsperuser==0)
print np.shape(U)

j=0
for i in range(s[0]):
    item=rawdata[i][1]
    user=rawdata[i][0]
    if (item in L[0]) and (user in U[0]):
        rawdata1.append(rawdata[i])
        j=j+1



np.savetxt("data\\red_ratings_data.txt",rawdata1,delimiter='\t')

    
        



    
    

