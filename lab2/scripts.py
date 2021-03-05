from math import sqrt
import sys
import numpy as np

def cholesky(A):
    """Performs a Cholesky decomposition of A, which must 
    be a symmetric and positive definite matrix. The function
    returns the lower variant triangular matrix, L."""
    n = len(A)

    # Create zero matrix for L
    L = np.array([[0.0] * n for i in range(n)])

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): # Diagonal elements
                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
 
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
def solve_system2(A, b, x):
    for i in range (len(A),1,-1):
        sigma_sum = 0
        for j in range(i+1,len(A)+1):
            sigma_sum += A[i - 1, j - 1] * x[j - 1]
        x_i = (b[i - 1] - sigma_sum) / A[i-1, i-1]
        x[i-1] = x_i
    return(x)

def solve_system(A, b, x):
    for i in range(1, len(A) + 1):
        sigma_sum = 0
        for j in range(1, i):
            sigma_sum += A[i - 1, j - 1] * x[j - 1]
        x_i = (b[i - 1] - sigma_sum) / A[i - 1, i - 1]
        x = np.append(x, x_i)
    print(solve_system2(A,b,x))
