# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 12:44:14 2014

@author: Divya
"""

import numpy as np
data=np.genfromtxt("my_ratings.txt",delimiter=' ',dtype=int)
list_size = rawdata.shape[0]



item_adj_list=dict.fromkeys(data[:,1],None)
for i in item_adj_list.keys():
    item_adj_list[i]=[]

for i in range(list_size):
    item_adj_list[data[i][1]].append((data[i][0],data[i][2]))
    
print(item_adj_list)    


user_adj_list=dict.fromkeys(data[:,0],None)
for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(list_size):
    user_adj_list[data[i][0]].append((data[i][1],data[i][2]))
    
print(user_adj_list)    