x 2.a
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
    sum = abs(tan(x) - my_tan(x, 1000))
t2 = time.time()

time = t2 - t1
err = sum / 10000
print(time)
print(err)
