from numpy import *
import numpy as np
from scipy import stats as st
from ItemBasedRecommendation import get_training_data
from TrustDataPoll import get_training_trust_data
import rand 
import timeit
#   Initializing the matrix to all zeros for No of users = 49290 items = 139739
s = (49290,139739)
num_users=49290
# trust_matrix = [[0 for col in range(139737)] for row in range(49289)]
trust_matrix = np.zeros((num_users,num_users))
user_avg_trust_matrix=np.zeros(num_users)

#Building training data samples
# Converted the training input data from file to an integer matrix
def get_user_trust_matrix():
    global trust_matrix, num_users
    data = np.load("trust_network.npy")
    size =(num_users, num_users)
    user_item_matrix= np.zeros(size)
    for j in range(data.shape[0]):
        trust_matrix[data[j][0]][data[j][1]]=data[j][2]
    return trust_matrix
#Genetrust the trust matrixget_user_trust_matrix()
get_user_trust_matrix()
user_item_matrix = get_training_trust_data("sample_user_item_training.txt")

def get_trust(user,item):
    global user_item_matrix, trust_matrix
    depth = 0
    r_prob = 1
    avg_rating = 0
    den_prob = 0
    for n in range(10000):
    user_j = i
    while depth <= 3:
        depth = depth+1
        trusted_users_i = which(trust_matrix[user_j,:]>0)
        total_trust = len(trusted_users_i)
        user_j = rand.randint(range(total_trust))
        r_prob = r_prob*total_trust
        if user_item_matrix[user_j][i] > 0:
            avg_rating = avg_rating + user_item_matrix[user_j][i]*r_prob
            den_prob = den_prob + r_prob
            break
 
