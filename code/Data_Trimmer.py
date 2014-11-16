
# coding: utf-8

# In[3]:

import numpy as np
from copy import deepcopy

data=np.genfromtxt("data/ratings_data.txt",delimiter=' ',dtype=int)
print data.shape[0]


# In[5]:

list_size = data.shape[0]
item_adj_list=dict.fromkeys(data[:,1],None)
for i in item_adj_list.keys():
    item_adj_list[i]=[]

for i in range(list_size):
    item_adj_list[data[i][1]].append((data[i][0],data[i][2]))
    


# In[6]:

print item_adj_list[1]


# In[7]:

dup=deepcopy(item_adj_list)
for i in dup.keys():
    if(len(item_adj_list[i])<=2):
        del item_adj_list[i]


# In[8]:

print len(item_adj_list.keys())
print len(dup.keys())


# In[10]:

open('trimmed_items_ratings.txt', 'w').close()
for i in item_adj_list.keys():
    for l in item_adj_list[i]:
        u,r = l
        p = str(u) +" "+ str(i)+" "+str(r)+"\n"
        with open('trimmed_items_ratings.txt', 'a') as f:    
             f.write(p)


# In[11]:

userdata = np.genfromtxt("trimmed_items_ratings.txt",delimiter=' ',dtype=int)


# In[12]:

user_adj_list=dict.fromkeys(userdata[:,0],None)
list_user_size = userdata.shape[0]
for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(list_user_size):
    user_adj_list[userdata[i][0]].append((userdata[i][1],userdata[i][2]))
    


# In[13]:

print len(user_adj_list.keys())


# In[ ]:



