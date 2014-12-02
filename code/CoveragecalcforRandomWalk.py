
"""
Created on Sat Nov 29 22:30:35 2014

@author: Divya
"""

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
