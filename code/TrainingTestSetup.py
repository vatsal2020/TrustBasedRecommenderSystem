from ReservoirSample import get_random
import numpy as np


# Sample the user ratings from the Input files
data=np.genfromtxt("data/trimmed_items_ratings.txt",delimiter=' ',dtype=int)

datasize=data.shape[0]
testsize=int(.2*datasize)
trainsize=datasize-testsize

#generating training & test indices using reservoir sampling
sample_user_item_training =np.zeros((trainsize,3))
sampled_user_item_data = np.array(get_random(datasize,trainsize))

ind=np.zeros(datasize)
ind[sampled_user_item_data]=1
sample_user_item_test =np.zeros((testsize,3))
sample_user_item_training=data[ind==1]
sample_user_item_test=data[ind==0]


# writing the trimmed training data 
open('trimmed_training.txt', 'w').close()
for i in range(trainsize):
    p = str(sample_user_item_training[i][0]) +" "+ str(sample_user_item_training[i][1])+" "+str(sample_user_item_training[i][2])+"\n"
    with open('trimmed_training.txt', 'a') as f:
        f.write(p)

# writing the trimmed test data 
open('trimmed_test.txt', 'w').close()
for i in range(testsize):
    p = str(sample_user_item_test[i][0]) +" "+ str(sample_user_item_test[i][1])+" "+str(sample_user_item_test[i][2])+"\n"
    with open('trimmed_test.txt', 'a') as f:
        f.write(p)



