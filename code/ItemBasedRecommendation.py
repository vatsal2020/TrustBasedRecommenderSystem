from ReservoirSample import get_random
import numpy as np

# Sample the user ratings from the Input files


def get_training_data():
    data = []

    rawdata=np.genfromtxt("data/ratings_data.txt",delimiter=' ',dtype=None, names=True)

#print np.shape(rawdata)[0]

    size = (664823,3)
    data= np.zeros(size)
    p=0;
    for i in range(664823):
        data[i][0]=rawdata[i][0]
        data[i][1]=rawdata[i][1]
        data[i][2]=rawdata[i][2]

#   print data[1:10]

    size = (581720,1)
    sampled_user_item_data = np.zeros(size)
    size = (581720,3)
    sample_user_item_training =np.zeros(size)
#Sampling the input data using reservoir sampling n = 664824 , k = 581721
    sampled_user_item_data = np.array(get_random(664823,581720))

#print np.shape(sampled_user_item_data)[0]

    for i in  range(581720):
        sample_user_item_training[i][0] = data[sampled_user_item_data[i]][0]
        sample_user_item_training[i][1] = data[sampled_user_item_data[i]][1]
        sample_user_item_training[i][2] = data[sampled_user_item_data[i]][2]
#   print sample_user_item_training[1:10]

    return sample_user_item_training



# Unncomment this for getting the test data
#size=(83103,3)
#p=0
#sample_user_item_test =np.zeros(size)
#sampled_user_item_data_sorted = np.sort(sampled_user_item_data)

#j=0
#for i in  range(664823):
#    if (i == sampled_user_item_data_sorted[j]):
#j=j+1
        #    else:
        #        sample_user_item_test[p][0] = data[i][0]
        #sample_user_item_test[p][1] = data[i][1]
        #sample_user_item_test[p][2] = data[i][2]
#p =p+1
#print sample_user_item_test[0]



