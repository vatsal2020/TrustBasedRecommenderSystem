from ReservoirSample import get_random
import numpy as np

# Sample the user ratings from the Input files
data = []
rawdata=np.genfromtxt("data/ratings_data.txt",delimiter=' ',dtype=None, names=True)
size = (664823,3)
data= np.zeros(size)
p=0;
for i in range(664823):
    data[i][0]=rawdata[i][0]
    data[i][1]=rawdata[i][1]
    data[i][2]=rawdata[i][2]
size = (581720,1)
sampled_user_item_data = np.zeros(size)
size = (581720,3)
sample_user_item_training =np.zeros(size)
sampled_user_item_data = np.array(get_random(664823,581720))
ind=np.zeros(664823)
ind[sampled_user_item_data]=1
size_test = (83103,3)
sample_user_item_test =np.zeros(size_test)
sample_user_item_training=data[ind==1]
sample_user_item_test=data[ind==0]
print sample_user_item_training[0]
print sample_user_item_test[0]

# Saving the test data and the training and the test into npy files
np.save("training",sample_user_item_training)
np.save("test",sample_user_item_test)

