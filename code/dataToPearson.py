###Pearson correlation##
import numpy as np


A = np.random.randint(5,size=(10,20));
def common_users(i,j):
    col1 = A[i,:]
    col2 = A[j,:]
    subset = (col1>0)&(col2>0)
    rating = A[[[i],[j]],subset]
    return(rating)

 
