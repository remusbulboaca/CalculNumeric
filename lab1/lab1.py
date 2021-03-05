import math
import random
import time
# Ex 1
def ex1():
    m = -1
    mach = 0
    while 1:
        if 1.0 + 10**m == 1.0:
            mach = 10**m
            break
        m = m - 1
    mach = 10**(m+1)
    return mach

#Ex 2.a
def ex2a():
    a = 1.0
    b = ex1()/10
    c = ex1()/10
    if (a + b) + c == a + (b + c):
        return "[ + C ] Asociativa"
    else:
        return "[ + C ] Neasociativa"

#Ex 2.b
def ex2b():
    a = 0.2
    b = ex1()/10
    c = ex1()/10
    if (a * b) * c == a * (b * c):
        return "[ X C ] Asociativa!"
    else:
        return "[ X C ] Neasociativa!"


