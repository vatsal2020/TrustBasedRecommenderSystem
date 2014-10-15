from ReservoirSample import get_random

# Sample the user ratings from the Input files

data = []
data = [line.strip() for line in open("data/ratings_data.txt","r")]

sampled_user_item_data=[]

#Sampling the input data using reservoir sampling n = 664824 , k = 581721
sampled_user_item_data = get_random(664824,581721)

#writing the data samples (training data) to a file
file = open("sample_user_item_training.txt","w")
for i in range(0,581720):
    file.write(data[sampled_user_item_data[i]]+"\n")

#closing the file
file.close()

# creating a test data file
file1 = open("sample_user_item_test.txt","w")
for i in range(0,664824):
    if i not in sampled_user_item_data:
        file1.write(data[i]+"\n")
file1.close()


# Build the correlation matrix for the sampled input values
