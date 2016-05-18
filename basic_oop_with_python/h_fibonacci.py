'''
Project:            Basic OOP with Python
Dependent files:    2-main.py

The function in this file computes the fibonacci number of
a given number. In this method, recursion has been used.

Gloria Bwandungi, 2016.
'''

def fibonacci(n):
    if n == 0:                                       #special case for 0
        return 0
    elif n == 1:                                     #special case for 1
        return 1
    elif n > 1:
        return (fibonacci(n - 2) + fibonacci(n - 1)) #for +ve values of n
    elif n == -1:                                    #special case for -1
        return 1
    elif n < -1:
        return (fibonacci(n + 2) - fibonacci(n + 1)) #for -ve values of n
