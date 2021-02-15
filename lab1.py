eps = 1.0

while((1.0 + 0.5*eps)!=1.0):
    eps = 0.5 * eps

print("Valoare precizie masina : ", eps)

a = 1.0
b = eps / 10
c = eps / 10

sum1 = a * b
print("[SUM1] a + b :", sum1)
sum1 = sum1 * c

sum2 = b * c 
print("[SUM2] b + c :",sum2)
sum2 = sum2 * a

print("Suma ( a + b ) + c = ", sum1)
print("Suma a + ( b + c ) = ", sum2)
