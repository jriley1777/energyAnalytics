'''
Created on Apr 6, 2013

@author: Joseph Riley
'''

## Energy Analytics - Assignment 1 - Python Intro

print("Question 1 - NPV")
## Question 1:
## Write a function that takes as input:
##   a. Number of years
##   b. Initial value of and investment
##   c. Internal rate of return
## and it returns the NPV value. Report the result for years = 20, investment = $1m, rate = 4%.

def efv(numYears, initVal, IRR):
    #npv is the discounted future cash flows (payments) usually offset by the initial investment outlay
    #with these inputs, we must solve for the future expected value.
    #netpv = futureValue/pow((1+IRR),numYears)
    netfv = (initVal*pow((1+IRR),numYears))
    print ("For ${:,.2f}".format(initVal)+" compounded yearly for "+str(numYears)+" years with an annual rate of return at "+str(IRR)+"%,")
    #print ("The net present value is ${:,.2f}".format(netpv))
    print ("The future expected value is ${:,.2f}".format(netfv))

efv(20,1000000,.04)

print("")
print("Alternatively, if we consider 1,000,000 to be the expected value in 20 years, what is the present value with a discount rate of .04%?")

def npv(numYears, initVal, IRR):
    netpv = (initVal/pow((1+IRR),numYears))
    print ("The present value of ${:,.2f}".format(initVal)+", "+str(numYears)+" years from today, assuming a rate of "+str(IRR)+"%, is ${:,.2f}".format(netpv))
npv(20,1000000,.04)

print("")
print("Question 2 - Bubble Sort")
## Question 2.
## Bubble sort is an easy (but inefficient) method to sort a list. It scan a pairs of numbers in the list.
## Whenever a pair that is not in order is found, the two numbers are swapped.
## Implement bubble sort (it should only work on lists).

## We need two pointers:  one for the element i and another for element i+1
def sort(myList): # Bubble Sort Algorithm
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] > myList[j]:
                #double assignment to do the swap
                myList[i], myList[j]  = myList[j], myList[i]

    print "The new sorted list is "+str(myList)
    
badList = [2,5,4,3,25,22,21,5252]
print("The input is "+str(badList))
sort(badList)

print("")
print("Question 3 - Palindromes")
## Question 3.
## Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same
## written backwards). For example, is_palindrome("radar") should return True.

def is_palindrome(stringToTest):
    lowered = stringToTest.lower().strip().replace(' ', '')
    palindrome = 'True'
    for i in range(0,len(lowered),1):
        #default is true and we look for a false case 
        #between a letter some distance from the start and same distance from the end
        #i must equal -i but we must consider the zero indexing so adjust -i by -1
        if lowered[i]!=lowered[-i-1]:
            palindrome = 'False'
    print lowered, palindrome

is_palindrome("heLlO Olle h")
is_palindrome("racecar")
is_palindrome("Raceecar")
is_palindrome("joeriley")
is_palindrome("abbaabba")
is_palindrome("true")
is_palindrome("tacocat")

print("")
print("Question 4 - Procedural Histogram")

## Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
## For example, histogram([4, 9, 7]) should print the following:
## ****
## *********
## *******

def histogram(numList):
    print numList
    for i in numList:
        print i*'*'

myList = [3,7,8,25,23,13,6]
histogram(myList)