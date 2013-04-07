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

def npv(numYears, initVal, IRR):
    #netpv = futureValue/pow((1+IRR),numYears)
    netfv = (initVal*pow((1+IRR),numYears))
    print ("For ${:,.2f}".format(initVal)+" compounded yearly for "+str(numYears)+" years with an annual rate of return at "+str(IRR)+"%,")
    #print ("The net present value is ${:,.2f}".format(netpv))
    print ("The future expected value is ${:,.2f}".format(netfv))


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
                myList[j], myList[i]  = myList[i], myList[j]

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