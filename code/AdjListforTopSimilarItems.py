# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 17:23:12 2014

@author: Divya
"""

import numpy as np
from copy import deepcopy

data=np.genfromtxt("data/trimmed_items_ratings.txt",delimiter=' ',dtype=int)
data.shape
data=data[range(500),:]

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
    if (len(commonusers)<2):
        return -2
    for l in range(len(commonusers)):
       useriratings.append(item_adj_list[i][userini.index(commonusers[l])][1]-user_averages[commonusers[l]])
       userjratings.append(item_adj_list[j][userinj.index(commonusers[l])][1]-user_averages[commonusers[l]])
    #print(useriratings)
    #print(userjratings)
    num=np.dot(useriratings,userjratings)
    deno1=np.sqrt(np.dot(useriratings,useriratings))
    deno2=np.sqrt(np.dot(userjratings,userjratings))
    deno = deno1*deno2
    if (deno !=0):
        #print( num*1.0/deno)
        return ( num*1.0/deno)
    else:
        return -2
      
simij=pearson_corr(i,j)
print(simij)

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
                        
                    
                 
