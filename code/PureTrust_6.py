
# coding: utf-8

# In[1]:

import numpy as np
from numpy import random
import math
import random
from scipy.stats import itemfreq


# In[2]:

rating_data=np.genfromtxt("trimmed_items_ratings_10_10.txt",delimiter=' ',dtype=int)
rating_list_size = rating_data.shape[0]
trust_data = np.genfromtxt("data/trust_data 2.txt",delimiter=' ',dtype=int)
trust_list_size = trust_data.shape[0]


# In[3]:

item_adj_list=dict.fromkeys(rating_data[:,1],None)
for i in item_adj_list.keys():
    item_adj_list[i]=[]

for i in range(rating_list_size):
    item_adj_list[rating_data[i][1]].append((rating_data[i][0],rating_data[i][2]))
   
user_adj_list=dict.fromkeys(rating_data[:,0],None)
for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(rating_list_size):
    user_adj_list[rating_data[i][0]].append((rating_data[i][1],rating_data[i][2]))
    


# In[4]:

trust_list=dict.fromkeys(trust_data[:,1],None)
for i in trust_list.keys():
    trust_list[i]=[]

for i in range(trust_list_size):
    trust_list[trust_data[i][0]].append(trust_data[i][1])


# In[5]:

trust_list_cl = dict.fromkeys(filter(set(trust_data[:,0]).__contains__, user_adj_list.keys()))
for i in trust_list_cl.keys():
    trust_list_cl[i]= trust_list[i]


# In[6]:

testdata = np.genfromtxt("trimmed_test_10_10.txt",delimiter=' ',dtype=int)


# In[7]:

coverage_count = 0;
def get_rating_trust(user,item,n_iter):
    global rating_list, trust_list, user_list, coverage_count
    mean_rating = 0.0
    ##Dont know what this does##
    if user not in user_adj_list.keys():
        return -2;
    depth = 0
    r_prob = 1.0        
    den_prob = 0.0
    sum_rating =0.0
    avg_rating = 0.0
    sum_count = 0.0
    for n in range(n_iter):
        depth = 0
        r_prob = 1.0
        user_j = user
        while depth <=5:
            depth = depth+1
            # Find the index of all users which user_j trusts or break if that user is not there in the trust list
            if user not in trust_list.keys():
                break
            trusted_users_j = trust_list[user]
          
            
            ##find which fn## which(trust_matrix[user_j,:]>0)
            total_trust = len(trusted_users_j)
            if total_trust == 1:
                break
            else: 
                #user_j = random.randint(range(total_trust))
                #Pick a random user j from the set of selected indices
                if len(trusted_users_j) == 0:
                    break
                else:
                    random_index = random.randint(0,len(trusted_users_j)-1)  
                    user_j = trusted_users_j[random_index]
                
              
             #Probability with which user_j was picked
            r_prob = r_prob * 1/total_trust
            
            #Update the numerator and the denominator to find the avg rating of the item i
            #print user_j, item, list(zip(*item_adj_list[item]))
            if user_j in list(zip(*item_adj_list[item]))[0]:
                temp_rating = list(zip(*item_adj_list[item]))[1][list(zip(*item_adj_list[item]))[0].index(user_j)]
                sum_rating = sum_rating + temp_rating
                sum_count = sum_count +1
               # print r_prob, temp_rating
                den_prob = den_prob + r_prob
                break
        #print user_j, item
    if den_prob ==0.0:
        return -2
        #print 5
    else:
        avg_rating = sum_rating/sum_count
        coverage_count = coverage_count +1
    return(avg_rating)



# In[8]:


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


# In[9]:

numpreds=0
sumerr=0.0
            
def RMSE(n_iter):
    global user_adj_list_test,item_adj_list_test, numpreds, sumerr
    RMSE_Trust= 0;
    count =0;
    # Calculates the error in rating contributed by each (user, item) pair in the test data
    for user in user_adj_list_test.keys():
        if(trust_list.has_key(user)):
            for j in range(len(user_adj_list_test[user])):
                item=user_adj_list_test[user][j][0]
                if item_adj_list.has_key(item):
                    pr=get_rating_trust(user,item,n_iter)
                    if(pr!=-2):
                        temp = (pr-user_adj_list_test[user][j][1])
                        sumerr=sumerr+(temp * temp)
                        numpreds=numpreds+1
                        if(numpreds%1000 ==0): print numpreds
                else: 
                    continue
        else:
            continue
    RMSE=np.sqrt(sumerr/numpreds) 
    return RMSE


# In[10]:

RMSE_Trust_val = RMSE(100)


# In[11]:

RMSE_Trust_val


# In[13]:

numpreds/7500.0


# In[35]:

len(filter(set(trust_data[:,0]).__contains__, user_adj_list.keys()))


# In[68]:

trust_list[filter(set(trust_data[:,0]).__contains__, user_adj_list.keys())[1]]


# In[120]:

np.shape(test_data)[0]


# In[111]:




# In[ ]:



