import math
from math import pi,tan
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

def my_tan(x, eps):
  sign = 1
  if x < 0:
    x *= -1
    sign = -1
  mic = 10**(-12)
  c = f = mic
  d = 0
  j = 1
  a = x 
  while True:
    b = 2*(j-1) + 1
    d = max(b + a*d, mic)
    c = max(b + a/c, mic)
    a = -x**2
    d = 1 / d
    delta = c*d
    f = delta*f
    j = j + 1   
    if abs(delta - 1) <= eps: 
      break
  return sign*f

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

t1 = time.time()
for i in range(0,10000):
    x = random.uniform(-pi/2,pi/2)
    sum = abs(tan(x) - my_tan(x, ex1()))
t2 = time.time()

time = t2 - t1
err = sum / 10000
print(time)
print(err)
