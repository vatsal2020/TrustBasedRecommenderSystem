from numpy import *
import numpy as np
from scipy import stats as st
from ItemBasedRecommendation import get_training_data



#   Initializing the matrix to all zeros for No of users = 49290 items = 139739
s = (49290,139739)
# rating_matrix = [[0 for col in range(139737)] for row in range(49289)]
rating_matrix = np.zeros(s)
pearson_correlation_matrix =np.zeros(s)

#Building training data samples
# Converted the training input data from file to an integer matrix
def get_user_input_matrix():
    global rating_matrix
    size = (581720,3)
    data = np.zeros(size)
    data = (get_training_data())
    size =(49290,139739)
    user_item_matrix= np.zeros(size)
    for j in range(581720):
            rating_matrix[data[j][0]][data[j][1]]=data[j][2]
    return rating_matrix

#Generating the rating matrix
get_user_input_matrix()

# Takes as input i,j which are the indices for users and returns the common set of items rated both i and j
def get_common_item_indices(i,j):
    global rating_matrix
    col1 = rating_matrix[i,:]
    col2 = rating_matrix[j,:]
    subset = (col1>0)&(col2>0)
    rating = rating_matrix[[[i],[j]],subset]
    return(rating) ## returing the boolean values

def get_Pearson_Correlation_Matrix():
    global pearson_correlation_matrix
    for user in range(49290):
        for user1 in range(user+1,49290):
            temp =get_common_item_indices(user,user1)
            print temp
            pearson_correlation_matrix[user][user1]=st.pearsonr(temp[0], temp[1]) ### Getting error over here
    print pearson_correlation_matrix[0][1]



