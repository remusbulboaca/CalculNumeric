import math
import random
import time
# Ex 1
m = -1
while 1:
    if 1.0 + 10**m == 1.0:
        mach = 10**m
        break
    m = m - 1

print(mach)

#Ex 2.1

a = 1.0
b = mach/10
c = mach/10
if (a + b) + c == a + (b + c):
    print ("[ + C ] Asociativa")
else:
    print ("[ + C ] Neasociativa")

#Ex 2.2

a = 1.2
b = mach/10
c = mach/10
if (a * b) * c == a * (b * c):
    print ("[ X C ] Asociativa!")
else:
    print ("[ X C ] Neasociativa!")