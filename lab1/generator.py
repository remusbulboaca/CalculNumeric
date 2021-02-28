import numpy as np
import random
import math

def pi_generator(n):
    array = np.array([],object)
    for i in range(0,n):
        x = round(random.uniform(math.pi/4, math.pi/2),4)
        array = np.append(array,x)
    array.sort()
    return array

def pi_generator2(n):
    array = np.array([],object)
    for i in range(0,n):
        x = round(random.uniform(-math.pi/2, math.pi/2),4)
        array = np.append(array,x)
    array.sort()
    return array