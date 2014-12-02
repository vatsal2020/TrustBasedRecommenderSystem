
# coding: utf-8

# In[1]:

import numpy as np
from copy import deepcopy

data=np.genfromtxt("trimmed_items_ratings_10_10.txt",delimiter=' ',dtype=int)
#data=data[range(50000),:]

testdata=np.genfromtxt("trimmed_test_10_10.txt",delimiter=' ',dtype=int)
#testdata=testdata[range(5000),:]

item_adj_list=dict.fromkeys(data[:,1],None)


for i in item_adj_list.keys():
    item_adj_list[i]=[]

for i in range(data.shape[0]):
    item_adj_list[data[i][1]].append((data[i][0],data[i][2]))
    
 
    
user_adj_list=dict.fromkeys(data[:,0],None)

for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(data.shape[0]):
    user_adj_list[data[i][0]].append((data[i][1],data[i][2]))
    

    
user_averages=dict.fromkeys(data[:,0],0)

for i in user_averages.keys():
   user_averages[i]=np.average(list(zip(*user_adj_list[i]))[1])


# In[2]:

no_of_Test= 7500
item_adj_list_test=dict.fromkeys(testdata[0:no_of_Test,1],None)

for i in item_adj_list_test.keys():
   item_adj_list_test[i]=[]

for i in range(no_of_Test):
   item_adj_list_test[testdata[i][1]].append((testdata[i][0],testdata[i][2])) 

user_adj_list_test=dict.fromkeys(testdata[0:no_of_Test,0],None)

for i in user_adj_list_test.keys():
    user_adj_list_test[i]=[]

for i in range(no_of_Test):
    user_adj_list_test[testdata[i][0]].append((testdata[i][1],testdata[i][2]))    


# In[5]:

trustdata=np.genfromtxt("data/trust_data 2.txt",delimiter=' ',dtype=int)
trust_adj_list=dict.fromkeys(trustdata[:,0],None)
list_trust_size = trustdata.shape[0]
for i in trust_adj_list.keys():
    trust_adj_list[i]=[]

for i in range(list_trust_size):
        trust_adj_list[trustdata[i][0]].append(trustdata[i][1])


# In[28]:

print len(trust_adj_list.keys())
print len(user_adj_list.keys())
print len(item_adj_list.keys())
print user_adj_list_test[1][0]


# In[3]:

import math


def pearson_corr_user(i,j):
    if not(i in user_adj_list) or not(j in user_adj_list):  
        return -2
    itemini= list(zip(*user_adj_list[i]))[0]
    iteminj= list(zip(*user_adj_list[j]))[0]
    commonitems = filter(set(itemini).__contains__, iteminj)
    commonitems = filter(set(commonitems).__contains__, user_adj_list.keys())
    #print(commonusers)   
    useriratings=[]
    userjratings=[]
    citems = len(commonitems)
    if (citems == 0):
        return -2
    for l in range(citems):
       useriratings.append(user_adj_list[i][itemini.index(commonitems[l])][1]-user_averages[commonitems[l]])
       userjratings.append(user_adj_list[j][iteminj.index(commonitems[l])][1]-user_averages[commonitems[l]])
    #print(useriratings)
    #print(userjratings)
    num=np.dot(useriratings,userjratings)
    deno1=np.sqrt(np.dot(useriratings,useriratings))
    deno2=np.sqrt(np.dot(userjratings,userjratings))
    deno = deno1*deno2 *(1+math.exp(-((citems*1.0)/2)))
    if (deno !=0):
        #print( num*1.0/deno)
        return ( num*1.0/deno) 
    else:
        return -2
      



# In[6]:

coverage_count =0

def predictrating(user,item):
    trust_net_size=len(trust_adj_list[user])
    sumrating=0
    sumdenom=0
    for i in trust_adj_list[user]:
        if not(trust_adj_list.has_key(i)):
                continue
        for j in trust_adj_list[i]:
            if not(user_adj_list.has_key(j)):
                continue
            itemin= list(zip(*user_adj_list[j]))[0]
            ratingin= list(zip(*user_adj_list[j]))[1]
            try:
                ind=itemin.index(item)
                sim=pearson_corr_user(user,j)
                if(sim>.4):
                    sumrating=sumrating+(.5*(ratingin[ind]-user_averages[j]))
                    sumdenom=sumdenom+.5
            except ValueError:
                continue
        if not(user_adj_list.has_key(i)):
            continue
        itemin= list(zip(*user_adj_list[i]))[0]
        ratingin= list(zip(*user_adj_list[i]))[1]
        try:
            ind=itemin.index(item)
            sim=pearson_corr_user(user,i)
            if(sim>.4):
                sumrating=sumrating+(1.0*(ratingin[ind]-user_averages[i]))
                sumdenom=sumdenom+1.0
        except ValueError:
            continue     
    if (sumdenom==0):
        return -1
    return user_averages[user]+(sumrating*1.0/sumdenom)

#predict_rating(1,74)


# In[7]:

numpreds=0
sumerr=0.0
for user in user_adj_list_test.keys():
    if (trust_adj_list.has_key(user)):
        for j in range(len(user_adj_list_test[user])):
            item=user_adj_list_test[user][j][0]
            if item_adj_list.has_key(item):
                pr=predictrating(user,item)
                if(pr!=-1):
                    temp = (pr-user_adj_list_test[user][j][1])
                    sumerr=sumerr+(temp * temp)
                    numpreds=numpreds+1
                    if(numpreds%1000 ==0): print numpreds
            else: 
                continue
    else:
        continue
        
            
RMSE=np.sqrt(sumerr/numpreds) 


print RMSE
print numpreds/7500


# In[9]:

numpreds/7500.0


# In[ ]:



