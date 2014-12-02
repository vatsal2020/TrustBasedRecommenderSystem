
# coding: utf-8

# In[1]:

import numpy as np
import math
import random
from copy import deepcopy


# In[2]:

import numpy as np


data=np.genfromtxt("trimmed_training.txt",delimiter=' ',dtype=int)
#data=data[range(50000),:]

testdata=np.genfromtxt("trimmed_test_10_10.txt",delimiter=' ',dtype=int)
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


# In[4]:



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
      




def get_random_item(l):
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





def phip(u,i,k):
    maxsim=0
    dist = []
    #dist = [[] for x in xrange(len(user_adj_list[u]))]  
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
        val,pr = get_random_item(dist)
    return maxsim/(1+math.exp(-((k*1.0)/2))),val
   





# In[9]:

trustdata=np.genfromtxt("trust_data 2.txt",delimiter=' ',dtype=int)
trust_adj_list=dict.fromkeys(trustdata[:,0],None)
list_trust_size = trustdata.shape[0]
for i in trust_adj_list.keys():
    trust_adj_list[i]=[]

for i in range(list_trust_size):
        trust_adj_list[trustdata[i][0]].append(trustdata[i][1])


# In[10]:






# In[11]:




#print user_adj_list[user]
def random_walk(u,item):
    max_depth=6
    rating=0
    for i in range(max_depth+1):
        if not(user_adj_list.has_key(u)):
            rating=-1
            break
        prob,ritem=phip(u,item,i)
        #print "i =",i
        #print "prob=",prob
        if (random.uniform(0, 1)<prob):
            #print "ritem=",ritem
            uitems= list(zip(*user_adj_list[u]))[0]
            uratings= list(zip(*user_adj_list[u]))[1]
            rating=uratings[uitems.index(ritem)]
            #print "rating=",rating
            break
        else: 
            if not(trust_adj_list.has_key(u)):
                rating=-1
                break
            ind=random.randint(0,len(trust_adj_list[u])-1)
            u=trust_adj_list[u][ind]
            #print "u",u
    if (rating==0):
        rating=-1
    return rating


# In[12]:



# In[15]:

numpreds=0
sumerr=0
count=0
for user in user_adj_list_test.keys():
    if (user_adj_list.has_key(user)):
        for j in range(len(user_adj_list_test[user])):
            item=user_adj_list_test[user][j][0]
            if item_adj_list.has_key(item):
                nwalks=100
                successfulwalks=0
                sum_ratings=0
                for walk in range(nwalks):
                    rat=random_walk(user,item)
                    if not(rat==-1):
                        successfulwalks=successfulwalks+1
                        sum_ratings=sum_ratings+rat
                pr=-1
                if not(sum_ratings==0):
                    pr=sum_ratings*1.0/successfulwalks
                    temp = (pr-user_adj_list_test[user][j][1])
                    sumerr=sumerr+(temp * temp)
                    numpreds=numpreds+1
            else:
                continue
    else:
        continue
    count = count + 1
    if(count%10000 == 0):
        print count    
            
RMSE=np.sqrt(sumerr/numpreds) 
print "RMSE",RMSE


##Calculating coverage for first 500 users and items
user_adj_list_test=dict.fromkeys(testdata[:,0],None)

for i in user_adj_list_test.keys():
    user_adj_list_test[i]=[]

for i in range(testdata.shape[0]):
    user_adj_list_test[testdata[i][0]].append((testdata[i][1],testdata[i][2])) 



item_adj_list_test=dict.fromkeys(testdata[:,1],None)

for i in item_adj_list_test.keys():
    item_adj_list_test[i]=[]

for i in range(testdata.shape[0]):
    item_adj_list_test[testdata[i][1]].append((testdata[i][0],testdata[i][2]))    
    
coverage=0
denom=0

nusers=0
nitems=0
for i in user_adj_list_test.keys():
    nusers=nusers+1
    if (nusers>500):
        break
    if (user_adj_list.has_key(i)):
        nitems=0
        for j in item_adj_list_test.keys():
            nitems=nitems+1
            if(nitems>500):
                break
            if (item_adj_list.has_key(j)):
                denom=denom+1
                nwalks=1000
                for walk in range(nwalks):
                    rat=random_walk(i,j)
                    if not(rat==-1):
                        coverage=coverage+1
                        break


print "Coverage",coverage*1.0/denom
cov=coverage*1.0/denom

f=open('Results.txt', 'a')
f.write("RMSE:"+ str(RMSE)+"\n")
f.write("Coverage:"+ str(cov)+"\n")
f.close()
