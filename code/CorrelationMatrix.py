from numpy import *
import numpy as np

#Building training data samples
# Converting the training input data from a text file to an integer matrix
def get_user_input_matrix():
    
    user_item_matrix=[]
    data = [line.strip() for line in open("sample_user_item_training.txt","r")]
    
    for l in data:
            t=l.split(' ')
            user_item_matrix.append(t)
    
    user_item_matrix_i = [map(int, x) for x in user_item_matrix]
    return user_item_matrix_i


# Generating Associative Matrix representing rows as users, items as colums and the matrix element as the rating (R_{u,i} data)

def generate_user_item_rating_matrix():


#   Initializing the matrix to all zeros for No of users = 49290 items = 139739

    s = (49290,139739)
# rating_matrix = [[0 for col in range(139737)] for row in range(49289)]
    rating_matrix = np.zeros(s)

#getting the integer matrix of the training data set
    source_data =np.array(get_user_input_matrix())
    print("raw data")
    print(source_data.shape)

#generating user item matrix for the training data set
    for i in range(0,581720):
        row = source_data.item(i,0)
        col = source_data.item(i,1)
        rate = source_data.item(i,2)
        rating_matrix[row,col] = rate

    print rating_matrix
    return rating_matrix


# invoking the functions

#get_user_input_matrix()
generate_user_item_rating_matrix()