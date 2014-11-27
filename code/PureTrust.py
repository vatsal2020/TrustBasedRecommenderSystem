
# coding: utf-8

# In[3]:

import numpy as np
from numpy import random
import math
import random
from scipy.stats import itemfreq


# In[4]:

rating_data=np.genfromtxt("data/trimmed_items_ratings.txt",delimiter=' ',dtype=int)
rating_list_size = rating_data.shape[0]
trust_data = np.genfromtxt("data/trust_data 2.txt",delimiter=' ',dtype=int)
trust_list_size = trust_data.shape[0]


# In[5]:

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
    


# In[6]:

trust_list=dict.fromkeys(trust_data[:,1],None)
for i in trust_list.keys():
    trust_list[i]=[]

for i in range(trust_list_size):
    trust_list[trust_data[i][0]].append(trust_data[i][1])


# In[7]:

trust_list_cl = dict.fromkeys(filter(set(trust_data[:,0]).__contains__, user_adj_list.keys()))
for i in trust_list_cl.keys():
    trust_list_cl[i]= trust_list[i]


# In[8]:

coverage_count = 0;
def get_rating_trust(user,item,n_iter):
    global rating_list, trust_list_cl, user_list, coverage_count
    mean_rating = 0.0
    ##Dont know what this does##
    if user not in user_adj_list.keys():
        return -2;
    depth = 0
    r_prob = 1.0        
    den_prob = 0.0
    sum_rating =0.0
    avg_rating = 0.0
    for n in range(n_iter):
        depth = 0
        r_prob = 1.0
        user_j = user
        while depth <=2:
            depth = depth+1
            # Find the index of all users which user_j trusts or break if that user is not there in the trust list
            if user not in trust_list_cl.keys():
                break
            trusted_users_j = trust_list_cl[user]
          
            
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
                sum_rating = sum_rating + temp_rating*r_prob
               # print r_prob, temp_rating
                den_prob = den_prob + r_prob
                break
        #print user_j, item
    if den_prob ==0.0:
        return -2
        #print 5
    else:
        avg_rating = sum_rating/den_prob
        coverage_count = coverage_count +1
    return(avg_rating)



# In[9]:

test_data = np.genfromtxt("data/trimmed_test.txt",delimiter=' ',dtype=int)


# In[ ]:

def RMSE(n_iter):
    global test_data, coverage_count
    RMSE_Trust= 0;
    count =0;
    # Calculates the error in rating contributed by each (user, item) pair in the test data
    for i in range(0,np.shape(test_data)[0]): #np.shape(test_data)[0]
        if(i%10000 == 0):
            print i
        user = test_data[i][0]
        item = test_data[i][1]
        pred_rating = get_rating_trust(user,item,n_iter)
        rating = test_data[i][2]
        if pred_rating != -2:
            RMSE_Trust = RMSE_Trust + (pred_rating-rating)**2
            count=count+1
            

    RMSE_Trust = math.sqrt(RMSE_Trust/np.shape(test_data)[0])
    #np.shape(test_data)[0]
    return RMSE_Trust

RMSE_Trust_val = RMSE(10)
print RMSE_Trust_val, coverage_count


# In[ ]:

RMSE_Trust_val = RMSE(10)
