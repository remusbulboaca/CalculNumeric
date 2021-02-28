from tangenta import *
import time
from generator import *


def main(n, x):
    return tangenta(n, x)

start_time = time.time()
x = pi_generator2(100)
for i in x:
    print(abs(math.tan(i) - main( 5,i)))
print("--- %s seconds ---" % (time.time() - start_time))

print("--------------------------------")

start_time = time.time()
y = pi_generator(100)
for i in y:
    print(abs(math.tan(i) - 1/main( 5, math.pi/2 - i)))
print("--- %s seconds ---" % (time.time() - start_time))

