# pyfuncs03.py
# SPIS 2016 -- stubs for some sample functions

# The following function is provided for you as an example
# of how to write a Python function involving "or"
# This contains HINTS as to how to do the next function definition.

def isAdditivePrimaryColor(color):
    ''' if color one of 'red', 'green', or 'blue' then True, otherwise False'''

    return ((color == 'red') or (color == 'green') or (color == 'blue'))

# NOTE: the following will NOT work for isAdditivePrimaryColor:
#
# def isAdditivePrimaryColor(color):
#   return ( color == "red" or "green" or "blue" )
#
# Try it, and convince yourself that it doesn't work.
# Does it fail to compile, fail to run (python vomit), or just give the
#  wrong answer?    You may be surprised!
# Try it, then try to understand _why_ this doesn't do what you want
# Hints: 'or' is an operator, and it must take operands that are
# either True or False
# (color == "red") is either True or False.  What about the other operands?



### @@@ NOW, write a function called isSimpleNumeric(x)
### @@@ This should return true if x is either an integer (int in Python), or
### @@@   a floating point number (float in Python).  
### @@@ (We'll ignore the 'complex' type for purposes of this function.)
### @@@ Include a comment describing what the function returns 
### @@@ similar to the comments above the other function definitions
### @@@ in this file
### @@@ Hint: combine what you did for isString with the pattern you see
### @@@  at work in isPrimaryColor of combining boolean expressions with "or"

def isSimpleNumeric(x):
    if type(x) == int or type(x) == float:
        return True
    else:
        return False
