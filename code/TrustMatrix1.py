
# coding: utf-8

# In[1]:

from numpy import *
import numpy as np
from scipy import stats as st
#from ItemBasedRecommendation import get_training_data
from TrustDataPoll import get_training_trust_data
from numpy import random
import math
import random
#import timeit
#   Initializing the matrix to all zeros for No of users = 49290 items = 139739
s = (49290,139739)
num_users=49290
num_items = 139739
rating_matrix = np.zeros((num_users,num_items))


# In[ ]:




# In[2]:

print num_items


# In[4]:

def get_rating_matrix():
    global num_users, num_items
    num_training =581720
    num_test = 83103
    size = (num_training,3)
    data = np.zeros(size)
    data = np.load("training.npy", mmap_mode =None)
    size =(num_users,num_items)
    user_item_matrix= np.zeros(size)
    for j in range(581720):
        rating_matrix[data[j][0]][data[j][1]]=data[j][2]
    return rating_matrix
rating_matrix = get_rating_matrix()
#
# trust_matrix = [[0 for col in range(139737)] for row in range(49289)]
trust_matrix = np.zeros((num_users,num_users))
#user_avg_trust_matrix=np.zeros(num_users)

#Building training data samples
#This converts the trust data into a trust matrix
def get_user_trust_matrix():
    global trust_matrix, num_users
    data = np.load("trust_network.npy")
    size =(num_users, num_users)
    trust_matrix= np.zeros(size)
    for j in range(data.shape[0]):
        trust_matrix[data[j][0]][data[j][1]]=data[j][2]
    return trust_matrix

#Retrieve the rating matrix 
trust_matrix=get_user_trust_matrix()
np.save("trust", trust_matrix)


# In[6]:

global rating_matrix, trust_matrix
depth = 0
r_prob = 1         
avg_rating = 0  
den_prob = 0
sum_rating =0


# In[7]:

test_data = np.load('test.npy')


# In[111]:

avg_rating = 0
def get_rating_trust(user,item):
    global rating_matrix, trust_matrix,avg_rating
    depth = 0
    r_prob = 1         
    avg_rating = 0  
    den_prob = 0
    sum_rating =0
    for n in range(10):
        depth = 0
        r_prob = 1
        user_j = user
        while depth <= 6:
            depth = depth+1
            # Find the index of all users which user_j trusts
            trusted_users_j = np.where(trust_matrix[user_j,:]==1)
            ##find which fn## which(trust_matrix[user_j,:]>0)
            total_trust = len(trusted_users_j)
            if total_trust == 1:
                random_index = 0;
            elif total_trust ==0:
                break
            else: 
                #user_j = random.randint(range(total_trust))
                #Pick a random user j from the set of selected indices
                random_index = random.randint(0,np.shape(trusted_users_j)[1]-1)
            user_j = trusted_users_j[0][random_index]  
             #Probability with which user_j was picked
            r_prob = r_prob * 1/total_trust
            #Update the numerator and the denominator to find the avg rating of the item i
            
            if rating_matrix[user_j][item] > 0:
                sum_rating = sum_rating + rating_matrix[user_j][item]*r_prob
                den_prob = den_prob + r_prob
                break
        #print user_j, item
    if den_prob ==0:
        avg_rating = 0
    else:
        avg_rating = sum_rating/den_prob
    return(avg_rating)

def RMSE():
    global test_data
    RMSE_Trust= 0;
    # Calculates the error in rating contributed by each (user, item) pair in the test data
    for i in range(0,int(np.shape(test_data)[0])):
        user = test_data[i][0]
        item = test_data[i][1]
        pred_rating = get_rating_trust(user,item)
        rating = test_data[i][2]
        RMSE_Trust = RMSE_Trust + (pred_rating-rating)**2

    RMSE_Trust = math.sqrt(RMSE_Trust/np.shape(test_data)[0])
    return RMSE_Trust


# In[109]:

RMSE_Trust_val = RMSE()


# In[110]:

RMSE_Trust_val


# In[63]:




# In[52]:




# In[49]:




# In[ ]:



