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

# Ex 3

def fac(num): 
    if (num == 0): 
        return 1; 
  
    # To store factorial of a number 
    fact = 1; 
    for i in range(1, num + 1): 
        fact = fact * i; 
  
    # Return the factorial of a number 
    return fact; 
  
# Function to find tan(x) upto n terms 
def Tanx_expansion(terms, x):  
    # To store value of the expansion 
    sum = 0;  
    for i in range(1, terms + 1): 
        # This loops here calculate Bernoulli number 
        # which is further used to get the coefficient 
        # in the expansion of tan x 
        B = 0; 
        Bn = 2 * i; 
        for k in range(Bn + 1): 
            temp = 0; 
            for r in range(0, k + 1): 
                temp = temp + pow(-1, r) * fac(k) \
                    * pow(r, Bn) / (fac(r) * fac(k - r)); 
  
            B = B + temp / ((k + 1)); 
  
        sum = sum + pow(-4, i) * (1 - pow(4, i)) \
            * B * pow(x, 2 * i - 1) / fac(2 * i); 
  
    # Print the value of expansion 
    print("%.9f" %(sum)); 
  
# Driver code 
if __name__ == '__main__': 
    n, x = 5, 0.6; 
  
    # Function call 
    # n_list = []
    # Tanx_expansion(n, x)
    # x = random.random()
    # for i in range(100):
    #     n_list.append(random.random())
    # print(round(random.uniform(-math.pi/2, math.pi/2), 4))
    
    random_pi = []
    for i in range(0,100):
        x = round(random.uniform(-math.pi/2, math.pi/2),4)
        random_pi.append(x)
    random_pi.sort() 
    print(random_pi)


    start = time.time()
    for i in range(0,100):
        if(|math.tan(random_pi[i]) - Tanx_expansion( 5 ,random_pi[i])|):
            count + = count
    print(count)
    stop = time.time()
    print(stop-start)
    