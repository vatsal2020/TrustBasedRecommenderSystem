
# coding: utf-8

import numpy as np
from copy import deepcopy

data=np.genfromtxt("data/ratings_data.txt",delimiter=' ',dtype=int)

#Trimming Item ratings
list_size = data.shape[0]
item_adj_list=dict.fromkeys(data[:,1],None)
for i in item_adj_list.keys():
    item_adj_list[i]=[]

#Creating Item adjacency list
for i in range(list_size):
    item_adj_list[data[i][1]].append((data[i][0],data[i][2]))


dup=deepcopy(item_adj_list)
for i in dup.keys():
    if(len(item_adj_list[i])<=2):
        del item_adj_list[i]

# writing to a Trimmed Items file
open('trimmed_items_ratings.txt', 'w').close()
for i in item_adj_list.keys():
    for l in item_adj_list[i]:
        u,r = l
        p = str(u) +" "+ str(i)+" "+str(r)+"\n"
        with open('trimmed_items_ratings.txt', 'a') as f:
            f.write(p)

userdata = np.genfromtxt("trimmed_items_ratings.txt",delimiter=' ',dtype=int)

#Creating User adajacency lists
user_adj_list=dict.fromkeys(userdata[:,0],None)
list_user_size = userdata.shape[0]
for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(list_user_size):
    user_adj_list[userdata[i][0]].append((userdata[i][1],userdata[i][2]))


#Trimming Trust Ratings
trustdata=np.genfromtxt("data/trust_data 2.txt",delimiter=' ',dtype=int)
userkeys=np.hstack((trustdata[:,0],trustdata[:,1]))
trust_adj_list=dict.fromkeys(user_adj_list.keys(),None)
list_trust_size = trustdata.shape[0]
for i in trust_adj_list.keys():
    trust_adj_list[i]=[]

for i in range(list_trust_size):
    if (trustdata[i][0] in user_adj_list) & (trustdata[i][1] in user_adj_list):
        trust_adj_list[trustdata[i][0]].append(trustdata[i][1])

#Writing trimmed trust data to a file
open('trimmed_trust.txt', 'w').close()
for i in trust_adj_list.keys():
    for l in trust_adj_list[i]:
        with open('trimmed_trust.txt', 'a') as f:
            f.write(str(i)+" "+str(l)+"\n")


