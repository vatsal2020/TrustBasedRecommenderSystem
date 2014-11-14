# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 17:14:24 2014

@author: Divya
"""
import numpy as np
from copy import deepcopy

# Sample the user ratings from the Input files

#rawdata=np.genfromtxt("C:\\Users\\Divya\\Documents\\Coursework\\Data Mining\\Project\\code\\ratings_data.txt",delimiter=' ',dtype=int)
        
#3d Lists code
userratings=[]
data=np.genfromtxt("C:\\Users\\Divya\\Documents\\Coursework\\Data Mining\\Project\\code\\my_ratings.txt",delimiter=' ',dtype=int)
userno=1
userlist=[]
uiter=0
for i in range(data.shape[0]):
    if (data[i][0]==userno):
        userlist+=[[0]*2]
        userlist[uiter][0]=data[i][1]
        userlist[uiter][1]=data[i][2]
        print(userlist[uiter])
        uiter=uiter+1
    else:
        userratings+=[[[0]*2]*uiter]
        userratings[userno-1]=userlist
        print(userratings[userno-1])
        userlist=[]
        userno=deepcopy(data[i][0])
        uiter=0
        userlist+=[[0]*2]
        userlist[uiter][0]=data[i][1]
        userlist[uiter][1]=data[i][2]
        print(userlist[uiter])
        uiter=uiter+1
userratings+=[[[0]*2]*uiter]
userratings[userno-1]=userlist     
print(userratings[userno-1])       
        
        
        
        
    


