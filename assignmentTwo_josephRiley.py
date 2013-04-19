'''
Created on Apr 14, 2013

@author: Riles
'''
## Energy Analytics - Assignment 2 - Shortest Path Algorithm

#first step will be to create a random network
import numpy as np
import random as rand

#create cost matrix
numNodes = 11
cost = np.random.random_integers(low=-1,high=100,size=(numNodes,numNodes))
np.fill_diagonal(cost,0)
#print cost


#create sampling dictionary with arcs and labels
sampleNet = {0:{}}
labelstart=1000000
print sampleNet
#0 will be start and 1 will be end
sampleNet[0] = {'arcs':dict(zip(range(2,4),cost[0,range(2,4)])),'label':0}
print sampleNet
sampleNet[1]= {'arcs':{1:0},'label':labelstart}
print sampleNet
sample = []
for i in range(2,numNodes):
    sample = rand.sample((range(2,i)+range(i+1,numNodes)),numNodes/3) #avoid selecting i in sample
    unitcost = []
    for j in sample:
        unitcost.append(cost[i,j])
    sampleNet[i] = {'arcs':dict(zip(sample,unitcost)),'label':labelstart}
for i in range(numNodes-2,numNodes):
    sample = rand.sample((range(2,i)+range(i+1,numNodes)),numNodes/3-1)
    sample.append(1)
    unitcost = []
    for j in sample:
        unitcost.append(cost[i,j])
    sampleNet[i] = {'arcs':dict(zip(sample,unitcost)),'label':labelstart}

print sampleNet

#net={0:dict(arcs={},label=sys.maxint)}
#{0:{'arcs':{1:121,..},'label':10000}}

s=0
t=1
S=[]
print S
for i in range(len(sampleNet.keys())):
    sl = 1000000
    bn = None
    for j in range(len(sampleNet.keys())):
        if not j in S:
            if sampleNet[j]['label'] < sl:
                #print sampleNet[j]['label']
                sl = sampleNet[j]['label']
                bn = j
                
    S.append(bn)
    if 1 in S: break
    print S, sampleNet
    for z in sampleNet[bn]['arcs']:     
        for k,v in sampleNet[bn]['arcs'].items():
            sampleNet[k]['label'] = min(sampleNet[k]['label'],(sampleNet[bn]['label']+sampleNet[bn]['arcs'][k]))
#            print labelofk #cost of arc from bn to k: net[bn][arcs][k]

print sampleNet
print sampleNet[1]['label']