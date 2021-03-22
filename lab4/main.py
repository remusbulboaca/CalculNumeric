import numpy as np
def get_mtx(filename):
    a = []
    b = []
    c = []
    p = None
    q = None
    
    with open(filename, 'r') as f:
        n = f.readline()    
        p = f.readline()
        q = f.readline()
        f.readline()
        switch = 0
        a = []
        b = []
        c = []
        for line in f:
            if (line == '\n'):
                switch = switch + 1
                continue
            if (switch == 0):
                a.append(float(line.rstrip('\n')))
            if (switch == 1):
                b.append(float(line.rstrip('\n')))
            if (switch == 2):
                c.append(float(line.rstrip('\n')))
    return a,b,c,p,q

def check_not_zero(a):
    for item in a:
        if item == 0:
            return False
    return True
    
def read_f(filename):
    n = None
    data = []
    with open(filename, 'r') as f:
        n = f.readline()
        f.readline()
        for line in f:
            data.append(float(line.rstrip('\n')))
    return data

def diagonalaNenula(A,p):
    esp = 1e-10**p
    for i in range(len(A)):
        j = -1
        for l in range(len(A[i])):
            if i == A[i][l][1]:
                j = l
                break
        if j > 0 and A[i][j][0] - 0 > esp:
            return False

    return True

def formula3(a, b, c, f, x_GS):
    xi = 0
    delta_x = 0
    for i in range(len(a)-1):
        upper = 0
        if i ==0:
            upper =  f[i] - b[i] * x_GS[i]
        if i == len(a):
            upper = f[i] - c[i-1] * x_GS[i-1]
        else:
            upper = f[i] - b[i] * x_GS[i] - c[i-1] * x_GS[i-1]
        upper /= a[i]
        delta_x += abs(upper - x_GS[i]) ** 2
        x_GS[i] = upper
    
    return delta_x


def gauss_seidel(a,b,c,f):
    x_GS = np.zeros(len(f))
    k = 0
    epsilon = 10 ** -8
    while(True):
        delta_x = formula3(a,b,c,f,x_GS)

        k = k + 1

        if k == 10000 or delta_x < epsilon or delta_x > 10**8:
            break
    if(delta_x < epsilon):
        return x_GS
    else:
        return -1

a,b,c,p,q = get_mtx('res/a2.txt')
f = read_f('res/f2.txt')
print(len(f))

print(gauss_seidel(a,b,c,f))