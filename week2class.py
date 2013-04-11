'''
Created on Apr 11, 2013

@author: Riles
'''
#lambda - just like apply in R
x = [x*x for x in range(20) if x%3==0]
print x

print filter(lambda u: u <= 100, x)

#map
print map(lambda u: u+10, x)


###################
##################

#Strings

s = 'today is the very cold day'
print s.split() #tokenize a string
print s.split('o') #split on particular letter - tokenize based on specified delimiter

#variables
s = 'today the degree is %d in city %s' % (40,'Evanston')
print s

from csv import *
f = open('C:/Users/Riles/Documents/Northwestern/Projects/Feinberg/DataTables/active.csv','r')
cf = reader(f, delimiter = ',')
for x in cf:
    for y in x:
        print y

#############
# Afternoon Session
#############

##  NUMPY!!!

#u = range(3,5,.1) Gives an error - must call numpy

import numpy as np
a = np.array([1,3,5,6])
print a*2
print np.arange(3,5,.1)

#elements of an array have to be of the same type
#differing elements will be coerced into one data type
# i.e. if there is a string, then all will be strings

#matrix
a = [[1,2],[3,4]] #2x2 user defined matrix
print a
a = np.zeros((3,2),dtype=np.float) #matrix of zeros with data type float
print a

a = np.identity(3)
print a
b = a + 1 #executed element wise
c = 2 * b
c*c #not matrix multiplication - it's element by element squaring
d = np.dot(c,c)
#proper
print d

c = np.array([[1,2,44],[44,32,1],[34,21,4]])
import numpy.linalg as la


#####################
##  PANDAS
#####################

