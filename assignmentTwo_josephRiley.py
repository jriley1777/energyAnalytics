'''
Created on Apr 14, 2013

@author: Riles
'''
## Energy Analytics - Assignment 2 - Shortest Path Algorithm

#first step will be to create a random network
import numpy as np
import random as rand

##Even if this is inefficient, I figured I'd send along where my real effort was rather than just 
##reformating your pseudo code for the network.  I see that I can just avoid the cost matrix by using
##randn to get a probability for a given node, check if at or below .3, if so we generate a random integer
##between -1 and 100 as the arc cost.


def randNetwork(numNodes=np.random.randint(500,1000), inOutConnections=10):
    
    if numNodes < inOutConnections+2:
        print "Please provide a number greater than or equal to 12"
    
    else:
        
        #Cost reference start
        cost = np.random.randint(low=-1,high=100,size=(numNodes,numNodes))
        np.fill_diagonal(cost,0)
        #Cost reference end
        
        #Network start
        
        #create sampling dictionary with arcs and labels
        network = {0:{}}
        labelstart=1000000 #default label
        
        #0 will be start and 1 will be end
        network[0] = {'arcs':dict(zip(range(2,inOutConnections+2),cost[0,range(2,inOutConnections+2)])),'label':0}
        network[1]= {'arcs':{1:0},'label':labelstart}
        #print network
        sample = []
        for i in range(2,numNodes):
            sample = rand.sample((range(2,i)+range(i+1,numNodes)),numNodes/3) #avoid selecting i in sample
            unitcost = []
            for j in sample:
                unitcost.append(cost[i,j])
            network[i] = {'arcs':dict(zip(sample,unitcost)),'label':labelstart}
        for i in range(numNodes-(inOutConnections),numNodes):
            sample = rand.sample((range(2,i)+range(i+1,numNodes)),((numNodes/3)-1))
            sample.append(1)
            unitcost = []
            for j in sample:
                unitcost.append(cost[i,j])
            network[i] = {'arcs':dict(zip(sample,unitcost)),'label':labelstart}
        return network
    
#Network end

#Algorithm start

def shortpath(network):
    S=[]
    
    ##Working on figuring out how to write the path from this
    #minpath={}
    #for i in range(len(network.keys())): 
    #    minpath[i] = []
    #    minpath[i].append(0)
    
    
        
    #Change negative arc values
    print "Checking for negative arc costs..."
    for i in range(len(network.keys())): 
        for z in network[i]['arcs']:     
            for k,v in network[i]['arcs'].items():
                if v < 0:
                    print "There is a negative arc connection with node " + str(i)
                    print "Changing value to 1,000,000"
                    network[i]['arcs'][k] = 1000000
    print "Arc check complete"
                        
    for i in range(len(network.keys())):   
        sl = 1000000
        bn = None
        for j in range(len(network.keys())):
            if not j in S:
                if network[j]['label'] < sl:
                    sl = network[j]['label']
                    bn = j
                    
        S.append(bn)
        print S, network
        
        #find our new label
        for z in network[bn]['arcs']:     
            for k,v in network[bn]['arcs'].items():
                    network[k]['label'] = min(network[k]['label'],(network[bn]['label']+network[bn]['arcs'][k]))
                    #minpath[k] = bn    
                    
    #return statements
    if network[1]['label'] < 1000000:
        print "The shortest path distance is " + str(network[1]['label'])
    else:
        print "No possible path"

#Algorithm end

#default number of nodes is a random integer between 500 and 1000 nodes
#default in/out connections is 10

sampleNet = randNetwork(numNodes=12,inOutConnections=3)
print "Initial network connections"
print sampleNet
shortpath(sampleNet)