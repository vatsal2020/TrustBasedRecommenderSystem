from numpy import *
import numpy as np
from scipy import stats as st
from ItemBasedRecommendation import get_training_data
from TrustDataPoll import get_training_trust_data
from numpy import random
import math


#import rand 
#import timeit
#   Initializing the matrix to all zeros for No of users = 49290 items = 139739
s = (49290,139739)
num_users=49290
# trust_matrix = [[0 for col in range(139737)] for row in range(49289)]
trust_matrix = np.zeros((num_users,num_users))
%user_avg_trust_matrix=np.zeros(num_users)

#Building training data samples
#This converts the trust data into a trust matrix
def get_user_trust_matrix():
    global trust_matrix, num_users
    data = np.load("trust_network.npy")
    size =(num_users, num_users)
    rating_matrix= np.zeros(size)
    for j in range(data.shape[0]):
        trust_matrix[data[j][0]][data[j][1]]=data[j][2]
    return trust_matrix

#Retrieve the rating matrix 
trust_matrix=get_user_trust_matrix()
np.save("trust", trust_matrix)

rating_matrix = get_training_trust_data("sample_user_item_training.txt")

#Function which returns the trust value
def get_rating_trust(user,item):
    global rating_matrix, trust_matrix
    depth = 0
    r_prob = 1         
    avg_rating = 0  
    den_prob = 0
    sum_rating =0
    for n in range(10000):
	depth = 0
  	r_prob = 1         
        user_j = user
        while depth <= 6:
            depth = depth+1
            # Find the index of all users which user_j trusts
            trusted_users_j = np.where(trust_matrix[user_j,:]==1)
            ##find which fn## which(trust_matrix[user_j,:]>0)
            total_trust = len(trusted_users_j)
            #user_j = random.randint(range(total_trust))
            #Pick a random user j from the set of selected indices
            user_j =random.choice(trusted_users_j)
            #Probability with which user_j was picked
            r_prob = r_prob * 1/total_trust
            #Update the numerator and the denominator to find the avg rating of the item i
            if rating_matrix[user_j][item] > 0:
                sum_rating = sum_rating + rating_matrix[user_j][item]*r_prob
                den_prob = den_prob + r_prob
                break
            
    avg_rating = sum_rating/den_prob
    return(avg_rating)

test_data = np.load('test.npy')
def RMSE(test_data):
    global test_data
    RMSE_Trust= 0;
    # Calculates the error in rating contributed by each (user, item) pair in the test data
    for i in range(0,np.shape(test_data)[0])
        user = test_data[i][1]
        item = test_data[i][2]
        pred_rating = get_rating_trust(user,item)
        rating = test_data[i][3]
        RMSE_Trust = RMSE_Trust + (pred_rating-rating)**2

    RMSE_Trust = math.sqrt(RMSE_Trust/np.shape(test_data)[0])
    return RMSE_Trust

RMSE_Trust_val = RMSE(test_data)
            

        
            
        
 
