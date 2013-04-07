'''
Created on Apr 6, 2013

@author: Joseph Riley
'''

## Energy Analytics - Assignment 1 - Python Intro


## Question 1:
## Write a function that takes as input:
##   a. Number of years
##   b. Initial value of and investment
##   c. Internal rate of return
## and it returns the NPV value. Report the result for years = 20, investment = $1m, rate = 4%.

def npv(numYears, initVal, IRR):
    #netpv = futureValue/pow((1+IRR),numYears)
    netfv = (initVal*pow((1+IRR),numYears))
    print ("For ${:,.2f}".format(initVal)+" compounded yearly for "+str(numYears)+" years with an annual rate of return at "+str(IRR)+"%,")
    #print ("The net present value is ${:,.2f}".format(netpv))
    print ("The future expected value is ${:,.2f}".format(netfv))


npv(20,1000000,.04)

## Question 2.
## Bubble sort is an easy (but inefficient) method to sort a list. It scan a pairs of numbers in the list.
## Whenever a pair that is not in order is found, the two numbers are swapped.
## Implement bubble sort (it should only work on lists).

#def sort(myList):
#    for i in myList:
#        if(myList[i]>=myList[i+1]):
#            swap = myList[i + 1]
#            myList[i] = myList[i+1]
#            myList[i] = swap
#    return myList
#
#badlist = [3,4,2,1,45]
#sort(badlist)

def bubbleSort(numbers): # Bubble Sort Algorithm
    nums = list(numbers)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]

    print numbers
    
badlist = [2,5,4,3,25,22,21,5252]
bubbleSort(badlist)

