
# coding: utf-8

# In[ ]:




# In[1]:

import numpy as np
from numpy import random
import math
import random


# In[2]:

rating_data=np.genfromtxt("data/trimmed_items_ratings.txt",delimiter=' ',dtype=int)
rating_list_size = rating_data.shape[0]



trust_data = np.genfromtxt("data/trimmed_items_ratings.txt",delimiter=' ',dtype=int)
trust_list_size = rating_data.shape[0]


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

trust_list=dict.fromkeys(user_adj_list.keys(),None)
for i in trust_list.keys():
    trust_list[i]=[]

for i in range(trust_list_size):
    trust_list[trust_data[i][0]].append(trust_data[i][1])


# In[5]:


coverage_count = 0;
def get_rating_trust(user,item):
    global rating_list, trust_list, user_list, coverage_count
    mean_rating = 0
    if len(user_adj_list[user]) >0:
        mean_rating = 2.5;
    depth = 0
    r_prob = 1         
    den_prob = 0
    sum_rating =0
    for n in range(10000):
        depth = 0
        r_prob = 1
        user_j = user
        while depth <= 6:
            depth = depth+1
            # Find the index of all users which user_j trusts
            trusted_users_j = trust_list[user]
            ##find which fn## which(trust_matrix[user_j,:]>0)
            total_trust = len(trusted_users_j)
            if total_trust == 1:
                break
            else: 
                #user_j = random.randint(range(total_trust))
                #Pick a random user j from the set of selected indices
                random_index = random.randint(0,len(trusted_users_j)-1)  
            user_j = trusted_users_j[random_index]  
             #Probability with which user_j was picked
            r_prob = r_prob * 1/total_trust
            
            #Update the numerator and the denominator to find the avg rating of the item i
            #print user_j, item, list(zip(*item_adj_list[item]))
            if user_j in list(zip(*item_adj_list[item]))[0]:
                temp_rating = list(zip(*item_adj_list[item]))[1][list(zip(*item_adj_list[item]))[0].index(user_j)]
                sum_rating = sum_rating + temp_rating*r_prob
               # print r_prob, temp_rating
                den_prob = den_prob + r_prob
                break
        #print user_j, item
    if den_prob ==0:
        avg_rating = mean_rating
        coverage_count = coverage_count +1
        #print 5
    else:
        avg_rating = sum_rating/den_prob
    return(avg_rating)



# In[6]:

test_data = np.genfromtxt("data/trimmed_test.txt",delimiter=' ',dtype=int)


# In[7]:

def RMSE():
    global test_data
    RMSE_Trust= 0;
    # Calculates the error in rating contributed by each (user, item) pair in the test data
    for i in range(0,np.shape(test_data)[0]):
        if(i%10000 == 0):
            print i
        user = test_data[i][0]
        item = test_data[i][1]
        pred_rating = get_rating_trust(user,item)
        rating = test_data[i][2]
        RMSE_Trust = RMSE_Trust + (pred_rating-rating)**2

    RMSE_Trust = math.sqrt(RMSE_Trust/np.shape(test_data)[0])
    #np.shape(test_data)[0]
    return RMSE_Trust


# In[ ]:

RMSE_Trust_val = RMSE()


# In[ ]:

RMSE_Trust_val


# In[3]:

coverage_count


# In[ ]:



