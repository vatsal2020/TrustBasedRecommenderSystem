###Pearson correlation##
import numpy as np
from scipy import stats as st

A = np.random.randint(5,size=(10,20))
user_avg_rating_matrix=np.zeros(10)
def common_users(i,j):
    col1 = A[:,i]
    col2 = A[:,j]
    subset = (col1>0)&(col2>0)
    print subset
    print A
    rate_i = A[subset,i]
    rate_j = A[subset,j]
    pearson_correlation_matrix=st.pearsonr(rate_i,rate_j)
    print pearson_correlation_matrix[0]
#return(rating)

def pearson_corr(i,j):
    
    col1 = A[:,i]
    col2 = A[:,j]
    subset = (col1>0)&(col2>0) ## returing the boolean values
    rate_i = A[subset,i]
    rate_j = A[subset,j]
    print rate_i
    print rate_j
    user_avg=user_avg_rating_matrix[subset]
    print user_avg
    rate_i=rate_i-user_avg
    rate_j=rate_j-user_avg
    print rate_i
    print rate_j
    num=np.dot(rate_i,rate_j)
    print num
    deno1=np.sqrt(np.dot(rate_i,rate_i))
    print deno1
    deno2=np.sqrt(np.dot(rate_j,rate_j))
    print deno2
    deno = deno1*deno2
    if (deno !=0):
        print num/deno

def user_averages():
    global user_avg_rating_matrix
    for i in range(10):
        nne=np.count_nonzero(A[i])
        if(nne!=0):
            user_avg_rating_matrix[i]=np.sum(A[i])*1.0/nne


#print user_avg_rating_matrix
#common_users(1,2)
print "A"
print A

user_averages()
pearson_corr(1,2)
