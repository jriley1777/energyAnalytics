'''
Created on Apr 14, 2013

@author: Riles
'''
## Energy Analytics - Assignment 2 - Shortest Path Algorithm

#first step will be to create a random network
import pandas as pd
import numpy as np
import random as rand

numNodes = rand.randrange(500,1000)
data = np.array([np.arange(numNodes)]*numNodes)
df = pd.DataFrame(data, index=range(0,numNodes), columns=range(0,numNodes))
for i in df:
    for j in df:
        df[i][j] = rand.randrange(-1,100)
#now have data frame with distance matrix
print df.describe()

#need to sample nodeTo




        