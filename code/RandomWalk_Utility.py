import numpy as np
import math
import random
from copy import deepcopy

data=np.genfromtxt("data/trimmed_training.txt",delimiter=' ',dtype=int)
#data=data[range(50000),:]

testdata=np.genfromtxt("data/trimmed_test.txt",delimiter=' ',dtype=int)
#testdata=testdata[range(5000),:]

item_adj_list=dict.fromkeys(data[:,1],None)


for i in item_adj_list.keys():
    item_adj_list[i]=[]

for i in range(data.shape[0]):
    item_adj_list[data[i][1]].append((data[i][0],data[i][2]))
    
item_adj_list_test=dict.fromkeys(testdata[:,1],None)

for i in item_adj_list_test.keys():
    item_adj_list_test[i]=[]

for i in range(testdata.shape[0]):
    item_adj_list_test[testdata[i][1]].append((testdata[i][0],testdata[i][2]))    
    
user_adj_list=dict.fromkeys(data[:,0],None)

for i in user_adj_list.keys():
    user_adj_list[i]=[]

for i in range(data.shape[0]):
    user_adj_list[data[i][0]].append((data[i][1],data[i][2]))
    
user_adj_list_test=dict.fromkeys(testdata[:,0],None)

for i in user_adj_list_test.keys():
    user_adj_list_test[i]=[]

for i in range(testdata.shape[0]):
    user_adj_list_test[testdata[i][0]].append((testdata[i][1],testdata[i][2]))    
    
user_averages=dict.fromkeys(data[:,0],0)

for i in user_averages.keys():
   user_averages[i]=np.average(list(zip(*user_adj_list[i]))[1])

sim15=0
i=1
j=5

def pearson_corr(i,j):
    if not(i in item_adj_list) or not(j in item_adj_list):  
        return -2
    commonusers=[]
    userini= list(zip(*item_adj_list[i]))[0]
    userinj= list(zip(*item_adj_list[j]))[0]
    for l in range(len(userini)):
        if(userini[l] in userinj):
            commonusers.append(userini[l])
    #print(commonusers)   
    useriratings=[]
    userjratings=[]
    cusers=len(commonusers)
    if (cusers==0):
        return -2
    for l in range(cusers):
       useriratings.append(item_adj_list[i][userini.index(commonusers[l])][1]-user_averages[commonusers[l]])
       userjratings.append(item_adj_list[j][userinj.index(commonusers[l])][1]-user_averages[commonusers[l]])
    #print(useriratings)
    #print(userjratings)
    num=np.dot(useriratings,userjratings)
    deno1=np.sqrt(np.dot(useriratings,useriratings))
    deno2=np.sqrt(np.dot(userjratings,userjratings))
    deno = deno1*deno2*(1+math.exp(-((cusers*1.0)/2)))
    if (deno !=0):
        #print( num*1.0/deno)
        return ( num*1.0/deno)
    else:
        return -2
      
simij=pearson_corr(i,j)
print(simij)


simij=pearson_corr(1,61)
print(simij)


u=1
i=61
k=2

def phip(u,i,k):
    maxsim=0
    dist = []
    for l in user_adj_list[u]:
        sim=pearson_corr(i,l[0])
        if(sim!=-2): 
            dist.append((l[0],sim))#
        if(sim>maxsim):
            maxsim=sim
    val=-1
    if(len(dist)>0):
        items=list(zip(*dist))[0]# change
        sims=list(zip(*dist))[1]# change
        sims=sims/sum(sims)  
        dist=zip(items,sims)
        val,pr = random_distr(dist)
    return maxsim/(1+math.exp(-((k*1.0)/2))),val
   
p,pr=phip(u,i,k)
print pr
print p

def random_distr(l):
    assert l # don't accept empty lists
    r = random.uniform(0, 1)
    s = 0
    for i in xrange(len(l)):
        item, prob = l[i]
        s += prob
        if s >= r:
            l.pop(i) # remove the item from the distribution
            break
    else: # Might occur because of floating point inaccuracies
        l.pop()
    # update probabilities based on new domain
    d = 1 - prob
    t = deepcopy(l)
    for i in xrange(len(l)):
        p_b = l[i][1]/d
        t.append((l[i][0],p_b))
        del t[i]
    return item, t

dist = [(11, 0.5), (20, 0.25), (3, 0.05), (43, 0.01), (51, 0.09), (6, 0.1)]
val = random_distr(dist)
print val[0]

############################Original code for random probability below ###############

# In[36]:

#def random_distr(l):
 #   assert l # don't accept empty lists
  #  r = random.uniform(0, 1)
   # s = 0
    #for i in xrange(len(l)):
     #   item, prob = l[i]
      #  s += prob
       # if s >= r:
        #    l.pop(i) # remove the item from the distribution
         #   break
   # else: # Might occur because of floating point inaccuracies
    #    l.pop()
    # update probabilities based on new domain
    #d = 1 - prob 
    #for i in xrange(len(l)):
     #   l[i][1] /= d
    #return item, l

#dist = [[11, 0.5], [20, 0.25], [3, 0.05], [43, 0.01], [51, 0.09], [6, 0.1]]
#val, dist = random_distr(dist)
#print val    


# In[9]:




# In[ ]:



