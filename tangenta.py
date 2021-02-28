import numpy as np
import math

import math
import time

suma = 0

# Function to find tan(x) upto n terms
def Tanx_expansion(terms, x):
    # To store value of the expansion
    global suma
    suma = 0
    for i in range(1, terms + 1):
        # This loops here calculate Bernoulli number
        # which is further used to get the coefficient
        # in the expansion of tan x
        B = 0
        Bn = 2 * i
        for k in range(Bn + 1):
            temp = 0
            for r in range(0, k + 1):
                temp = temp + pow(-1, r) * math.factorial(k) * pow(r, Bn) / (math.factorial(r) * math.factorial(k-r))

            B = B + temp / (k + 1)

        suma = suma + pow(-4, i) * (1 - pow(4, i)) * B * pow(x, 2 * i - 1) / math.factorial(2 * i)
        # Print the value of expansion
    

def tangenta(n,x):
    Tanx_expansion(n,x)
    return suma