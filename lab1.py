## Ex1  precizie masina
def mach_precision():
    m = -1
    while 1:
        if 1.0 + pow(10,m) == 1.0:
            return pow(10,m)
        m = m - 1

print(mach_precision())

## Ex2.1
def non_associative():
    a = 1.0
    b = mach_precision()
    c = mach_precision()
    if (a + b) + c == a + (b + c):
        return "Asociativa!"
    else:
        return "NEAsociativa!"
## Ex2.2
def non_associative2():
    a = 1.2
    b = mach_precision()
    c = mach_precision()
    if (a * b) * c == a * (b * c):
        return "Asociativa!"
    else:
        return "NEAsociativa!"

print("Adunare : ", non_associative())
print("Inmultire : ", non_associative2())