
# coding: utf-8

# In[1]:

get_ipython().magic(u'load AdjListforTopSimilarItems.py')


# In[2]:


# In[1]:

import numpy as np
from copy import deepcopy

data=np.genfromtxt("data/trimmed_training.txt",delimiter=' ',dtype=int)
#data=data[range(50000),:]

testdata=np.genfromtxt("data/trimmed_test.txt",delimiter=' ',dtype=int)
#testdata=testdata[range(5000),:]

item_adj_list=dict.fromkeys(data[:,1],None)


for i in item_adj_list.keys():
    item_adj_list[i]=[]

for i in range(data.shape[0]):
    item_adj_list[data[i][1]].append((data[i][0],data[i][2]))
    
item_adj_list_test=dict.fromkeys(testdata[:,1],None)

for i in item_adj_list_test.keys():
    item_adj_list_test[i]=[]

for i in range(testdata.shape[0]):
    item_adj_list_test[testdata[i][1]].append((testdata[i][0],testdata[i][2]))    
    
user_adj_list=dict.fromkeys(data[:,0],None)

for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(data.shape[0]):
    user_adj_list[data[i][0]].append((data[i][1],data[i][2]))
    
user_adj_list_test=dict.fromkeys(testdata[:,0],None)

for i in user_adj_list_test.keys():
    user_adj_list_test[i]=[]

for i in range(testdata.shape[0]):
    user_adj_list_test[testdata[i][0]].append((testdata[i][1],testdata[i][2]))    
    
user_averages=dict.fromkeys(data[:,0],0)

for i in user_averages.keys():
   user_averages[i]=np.average(list(zip(*user_adj_list[i]))[1])


# In[ ]:

coverage=0
denom=0

for i in user_adj_list_test.keys():
    if (user_adj_list.has_key(i)):
        for j in item_adj_list_test.keys():
            if (item_adj_list.has_key(j)):
                denom=denom+1
                if not(predictrating(i,j)==-1):
                    coverage=coverage+1
                    



# In[4]:


import math
sim15=0
i=1
j=5

def pearson_corr(i,j):
    if not(i in item_adj_list) or not(j in item_adj_list):  
        return -2
    commonusers=[]
    userini= list(zip(*item_adj_list[i]))[0]
    userinj= list(zip(*item_adj_list[j]))[0]
    for l in range(len(userini)):
        if(userini[l] in userinj):
            commonusers.append(userini[l])
    #print(commonusers)   
    useriratings=[]
    userjratings=[]
    cusers = len(commonusers)
    if (cusers == 0):
        return -2
    for l in range(len(commonusers)):
       useriratings.append(item_adj_list[i][userini.index(commonusers[l])][1]-user_averages[commonusers[l]])
       userjratings.append(item_adj_list[j][userinj.index(commonusers[l])][1]-user_averages[commonusers[l]])
    #print(useriratings)
    #print(userjratings)
    num=np.dot(useriratings,userjratings)
    deno1=np.sqrt(np.dot(useriratings,useriratings))
    deno2=np.sqrt(np.dot(userjratings,userjratings))
    deno = deno1*deno2 *(1+math.exp(-((cusers*1.0)/2)))
    if (deno !=0):
        #print( num*1.0/deno)
        return ( num*1.0/deno) 
    else:
        return -2
      
simij=pearson_corr(i,j)
print(simij)


# In[6]:


#Reading data from top similar items
#topsimilardata=np.genfromtxt("data/top_similar_items.txt",delimiter=' ',dtype=int)
#top_similar_items =dict.fromkeys(topsimilardata[:,0],None)

#for i in top_similar_items.keys():
 #   top_similar_items[i]=[]

#for i in range(topsimilardata.shape[0]):
 #   top_similar_items[topsimilardata[i][0]].append((topsimilardata[i][1],topsimilardata[i][2]))   
    


# calculate similarity list for all items
top_similar_items =dict.fromkeys(data[:,1],None)

for i in top_similar_items.keys():
    top_similar_items[i]=[]

item_keys = top_similar_items.keys()
for i in item_keys:
    for j in item_keys:
        if not(i==j):
            similarity = pearson_corr(i,j);
            if not (similarity <0):
                if (len(top_similar_items[i])<=30):                
                    top_similar_items[i].append((j,similarity))
                else:
                    simvals=list(zip(*top_similar_items[i]))[1]
                    minsim=min(simvals)
                    minindex=simvals.index(minsim)
                    if (similarity>=minsim):
                        top_similar_items[i][minindex]=(j,similarity)
                        
               
open('top_similar_items.txt', 'w').close()
for i in top_similar_items.keys():
    for l in top_similar_items[i]:
        u,r = l
        p = str(i) +" "+ str(u)+" "+str(r)+"\n"
        with open('top_similar_items.txt', 'a') as f:    
             f.write(p)
            


# In[7]:

def predictrating(user,item):
    similarratings=[]
    itemrated=list(zip(*user_adj_list[user]))[0]
    for i in range(len(top_similar_items[item])):
        try:
            similarratings.append((top_similar_items[item][i][1],user_adj_list[user][itemrated.index(top_similar_items[item][i][0])][1]))
        except IndexError:
            continue
        except ValueError: # need to check 
            continue
    #print(len(similarratings))
    if(len(similarratings)<=2):
        return -1
    return np.dot(list(zip(*similarratings))[0],list(zip(*similarratings))[1])/sum(list(zip(*similarratings))[0])

print(predictrating(1,61))


# In[8]:



# RMSE calculation
numpreds=0
sumerr=0
for user in user_adj_list_test.keys():
    if (user_adj_list.has_key(user)):
        for j in range(len(user_adj_list_test[user])):
            item=user_adj_list_test[user][j][0]
            if item_adj_list.has_key(item):
                pr=predictrating(user,item)
                if(pr!=-1):
                    temp = (pr-user_adj_list_test[user][j][1])
                    sumerr=sumerr+(temp * temp)
                    numpreds=numpreds+1
            else:
                continue
    else:
        continue
        
            
RMSE=np.sqrt(sumerr/numpreds) 


print RMSE

print coverage

print denom



# In[9]:

print len(item_adj_list.keys())
print len(top_similar_items.keys())


# In[ ]:



