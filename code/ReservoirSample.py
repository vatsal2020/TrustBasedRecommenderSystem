#A function to randomly select k items from stream[0..n-1].
# Assumes K <= N, or this will never terminate

import random

def get_random(n,k):
    
    reservoir = [0 for x in range(k)]
    
    # reservoir[] is the output array.
    # Initialize reservoir with first k elements from population[]
    
    for i in range(0,k):
       reservoir[i] = i
            
    # Using a different seed value so that we don't get, same result each time we run this program
            
    random.seed()
                
    # Iterate from the (k+1)th element to nth element
                
    for i in range(k+1, n):
        j = random.randint(0,i)
                    
    # If the randomly picked index is smaller than k, then replace
    # the element present at the index with new element from population
        if(j < k) :
            reservoir[j] = i
                    
    return reservoir;

#print(get_random(10,5))