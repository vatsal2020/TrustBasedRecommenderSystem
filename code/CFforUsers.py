
# coding: utf-8

# In[1]:

import numpy as np
from copy import deepcopy

data=np.genfromtxt("trimmed_training_10_10.txt",delimiter=' ',dtype=int)
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


# In[2]:

from IPython.core.debugger import Tracer


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
      





#Reading data from top similar items
#topsimilardata=np.genfromtxt("data/top_similar_items.txt",delimiter=' ',dtype=int)
#top_similar_items =dict.fromkeys(topsimilardata[:,0],None)

#for i in top_similar_items.keys():
 #   top_similar_items[i]=[]

#for i in range(topsimilardata.shape[0]):
 #   top_similar_items[topsimilardata[i][0]].append((topsimilardata[i][1],topsimilardata[i][2]))   
    


# In[8]:

def predictrating(user,item):
    similarusers=[]
    corrs = []
    usr_avg_local = []
    userrated=list(zip(*item_adj_list[item]))[0]
    for j in userrated:
        corrs.append(pearson_corr_user(user,j))
        usr_avg_local.append(user_averages[j])
    posit_vals = np.array(corrs) >0
    #neget_vals = (np.array(corrs) <0)&(np.array(corrs)>-2)
    posit_corrs = np.array(corrs)[posit_vals]
    #neget_corrs = np.array(corrs)[neget_vals]
    rel_rating = np.array(list(zip(*item_adj_list[item]))[1])-usr_avg_local
    if(len(posit_corrs)<=5):
        return -1
    return user_averages[user] + (np.dot(posit_corrs, rel_rating[posit_vals]))/sum(posit_corrs)


# In[9]:

# RMSE calculation
##REgular function
numpreds=0
sumerr=0.0
for user in user_adj_list_test.keys():
    if (user_adj_list.has_key(user)):
        for j in range(len(user_adj_list_test[user])):
            item=user_adj_list_test[user][j][0]
            if item_adj_list.has_key(item):
                pr= predictrating(user,item)
                if(pr!=-1):
                    temp = (pr-user_adj_list_test[user][j][1])
                    sumerr=sumerr+(temp * temp)
                    numpreds=numpreds+1
                    if(numpreds%10000 ==0): print numpreds
            else: 
                continue
    else:
        continue
        
            
RMSE=np.sqrt(sumerr/numpreds) 


print RMSE
print numpreds/7500.0

print len(item_adj_list.keys())


# In[12]:

numpreds


# In[5]:




# In[ ]:

print RMSE

