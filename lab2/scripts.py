from math import sqrt
import numpy as np
from numpy.linalg import inv
import math

def verify_matrix(A):
    n = len(A)
    ok = True
    for i in range(n):
        for j in range(n):
            if A[i][j] < 0 :
                ok = False
    return ok

def cholesky(A):

    # returns the lower variant triangular matrix, L
    n = len(A)
    # Create zero matrix for L
    # L = np.array([[0.0] * n for i in range(n)])
    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(A[i][j] * A[k][j] for j in range(k))
            
            if (i == k): # Diagonal elements
                A[i][k] = math.sqrt(abs(A[i][i] - tmp_sum))
            else:
                A[i][k] = (1.0 / A[k][k] * (A[i][k] - tmp_sum))

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            A[i][j] = 0

    return A
 
# A = [[2.25, 3, 3], [3, 9.0625, 13], [3, 13, 24]]
# L = cholesky(A)

# print ("A:")
# pprint(A)

# print ("L:")
# pprint(L)

def transpusa(A):
    return A.transpose()

def determinant(A):
    return np.linalg.det(A)

def LLt_generate(L,Lt):
    n = len(L)
    LLt = np.array([[0.0] * n for i in range(n)])
    for i in range(n):
        for j in range(n):
            if i != j:
                LLt[i][j] = L[i][j]+ Lt[i][j]
            else:
                LLt[i][j] = L[i][j]
    return LLt
# def solve_system(L , b):
#     # if not determinant(L):
#     #     return 0
#     # for i in range(1,len(L)):
#     #     for j in range(i-1, len(L)):
#     #         print(L[i-1][j-1])
#     array = []
#     for i in range(0,len(L)):
#         for j in range(0,i+1):
#             array.append(L[i][j])
#     print(array)
#
#     for i in range(0,len(array)):
#
def solve_system2(A, b, x,epsilon):
    for i in range (len(A),1,-1):
        sigma_sum = 0
        for j in range(i+1,len(A)+1):
            sigma_sum += A[i - 1, j - 1] * x[j - 1]
        if not np.abs(A[i-1, i-1]) > epsilon:
            print("We can't solve the system.")
            return []
        x_i = (b[i - 1] - sigma_sum) / A[i-1, i-1]
        x[i-1] = x_i
    return(x)

def solve_system(A, b, x,epsilon):
    for i in range(1, len(A) + 1):
        sigma_sum = 0
        for j in range(1, i):
            sigma_sum += A[i - 1, j - 1] * x[j - 1]
        if not np.abs(A[i-1, i-1]) > epsilon:
            print("We can't solve the system.")
            return []
        x_i = (b[i - 1] - sigma_sum) / A[i - 1, i - 1]
        x = np.append(x, x_i)
    return solve_system2(A,b,x,epsilon)




def solution_check(A,xChol,b):
    # A_init*xChol
    C = A.dot(xChol)
    # euclidian distance
    dist = np.linalg.norm(C - b)
    print("{} < 10 ** (-8) {}\n".format(dist,dist < 10 ** (-8)))



# https://integratedmlai.com/matrixinverse/
def invert_matrix(A,epsilon):
    n = len(A)
    AM = A

    I = np.array([[0.0] * n for i in range(n)])
    for i in range(n):
        I[i][i] = 1

    IM = I

    indices = list(range(n))  # to allow flexible row referencing ***
    for fd in range(n):  # fd stands for focus diagonal
        if not np.abs(AM[fd][fd]) > epsilon:
            print("We can't solve the system.")
            return 0

        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd + 1:]:
            # *** skip row with fd in it.
            crScaler = AM[i][fd]  # cr stands for "current row".
            for j in range(n):
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM


