# pyfuncs05.py
# SPIS 2016 -- stubs for some sample functions

from pyfuncs04 import first
from pyfuncs04 import rest

# The function totalValue shows a recursive way to take a
# collection of numbers (a list such as [24,-5,78] or a tuple
# such as (3,6,9,-2), and find the total.
# 
# Note that the built-in Python function "sum" can be used instead,
# so this is here just as an example of a function such as "sum" might 
# be implemented with recursion, and the "first" and "rest" functions.

def totalValue(numbers):
    if len(numbers)==0:
        return 0
    else:
        return first(numbers) + totalValue(rest(numbers))
 
# The function productOfAll can be built in the same way as
# totalValue.  Try it:

def productOfAll(numbers):
    if len(numbers) == 0:
        return 1
    else:
        return first(numbers) * productOfAll(rest(numbers))

def isOdd(number):
  # Hint: use % operator.  If remainder after dividing by 2 is 1, its odd 
    return (number % 2 == 1)

def isEven(number):
    return (number %2 == 0)

# This function shows an example of counting things in a collection
# that meet some criterion

def countOdds(numbers):
    if len(numbers) == 0:
        return 0
    elif isOdd(first(numbers)):
        return 1 + countOdds(rest(numbers))
    else:
        return countOdds(rest(numbers))

# Use the pattern from countOdds as a hint, write a function
# that will find the sum of all the odd numbers in a collection
# 
# This can also be done with a loop (for loop, or while loop),
# but try to use recursion if you can.

def sumOdds(numbers):
    if len(numbers)==0:
        return 0
    if (isOdd(first(numbers))):
        return first(numbers) + sumOdds(rest(numbers))
    else:
        return sumOdds(rest(numbers))
