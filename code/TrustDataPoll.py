from ReservoirSample import get_random
import numpy as np
def get_training_trust_data(filepath):
    data = []

    rawdata=np.genfromtxt(filepath,delimiter=' ',dtype=None, names=True)

#print np.shape(rawdata)[0]

    size = (rawdata.shape[0],3)
    data= np.zeros(size)
    for i in range(rawdata.shape[0]):
        data[i][0]=rawdata[i][0]
        data[i][1]=rawdata[i][1]
        data[i][2]=rawdata[i][2]

    return data

