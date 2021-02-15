import numpy as np
## Ex 1
m = 0
u = int(input("U = "))
while(u > 0 and (1.0 + u != 1.0)):
    u = u / 10
    m = m + 1
print("Precizia masina: ")
print(u) ## precizia masina
print(m)

## Ex 2
print("Ex 2 ~~~~~~~~")

a = 1.0
b = u / 10
c = u / 10

print("b : " , b)
print("c : " , c)
var1 =  a + b 
print(var1)
var2 = a + ( b + c )
print(var2)
if(var1 == var2):
    print("Tata de mata")


print("Test")
t=1
while t+1>1:t/=2
print(t)

a1 = 1.0
b1 = t / 10
c1 = t / 10     

print("b1 : " , b1)
print("c1 : " , c1)

sum1 = a1 + (b1 + c1)
sum2 = (a1 + b1) + c1

print("sum1 : " , sum1)
print("sum2 : " , sum2)

print(a1 + t)