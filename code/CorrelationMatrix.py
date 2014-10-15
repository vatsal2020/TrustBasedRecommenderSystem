from numpy import *
import numpy as np

#Building Sampled training data
# Converted the training data element integer matrix
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
#No of user = 49290 items = 139738


#   Initializing the matrix to all zeros
    s = (49290,139738)
# rating_matrix = [[0 for col in range(139737)] for row in range(49289)]
    rating_matrix = np.zeros(s)
    print("0")

# for i in range(0,49289):
#       for j in range(0,139737):
#           rating_matrix.append(0)

#getting the integer matrix of the training data set
    source_data = get_user_input_matrix()

    for data in source_data:
        rating_matrix[data[0]][data[1]] = data[2]

    print(rating_matrix[1][100])

#get_user_input_matrix()
generate_user_item_rating_matrix()