import numpy as np
import random
import matplotlib.pyplot as plt
import  math

import sympy as sym
from sympy import *

def function_fx(x):
    return x**2-12*x+30

def generate_xi_values(inceput, final):
    vector = []
    vector.append(float(inceput))
    for i in np.arange(inceput+1, final):
        vector.append(random.uniform(i, i+0.5))
    vector.append(float(final))
    print("xi", vector)
    return vector

def generate_yi_values(vector):
    ys = []
    for i in range(len(vector)):
        ys.append(function_fx(vector[i]))
    print("yi:", ys)
    return ys

def generate_yi_trigonometric_values(vector):
    ys = []
    for i in range(len(vector)):
        ys.append(function_trig_fx(vector[i]))
    print("yi:", ys)
    return ys

def compute_matrix_b(x_values):
    matrix = np.zeros((len(x_values), len(x_values)), dtype=float)
    for i in range(len(x_values)):
        for j in range(len(x_values)):
            if j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = x_values[i]**j
    # print("matrix B", matrix)
    return matrix

def compute_ai(matrix, ys):
    ai_vec = np.linalg.solve(matrix, ys)
    print("ai:", ai_vec)
    return ai_vec

#Horner schema
def compute_Pm_not_x(ai_vec, x):
    #reverse to start from a_n
    ai_vec = ai_vec[::-1]
    d = 0
    for i in range(len(ai_vec)):
        d = ai_vec[i] + d*x
    return d

def plot_f():
    x = np.arange(1, 5, 0.1)
    y = x**2-12*x+30
    plt.title("f(x) plot")
    plt.plot(x, y)
    plt.show()

def plot_Pm(ai_vec):
    x = np.arange(1, 5, 0.1)
    y = ai_vec[0]
    for i in range(1, len(ai_vec)):
        for j in range(len(ai_vec),0,-1):
            y = y + ai_vec[i]*x**j
    plt.title("Pm(x) plot")
    plt.plot(x, y)
    plt.show()

def plot_Sf(aii_vec):
    x = np.arange(0, 2 * np.pi, 0.1)
    ai_vec = []
    for el in aii_vec:
        ai_vec.append(el)
    y = ai_vec[0]
    for i in range(1, len(ai_vec)):
        if i % 2 == 1:
            y = y + ai_vec[i] * np.sin(x * i)
        elif i % 2 == 0:
            y = y + ai_vec[i] * np.cos(x * i)
    plt.title("SF(x) plot")
    plt.plot(x, y)
    plt.show()



#fx = sinx-cosx
def function_trig_fx(x):
    return sym.sin(x) - sym.cos(x)

def derivata(x0):
    x= sym.symbols('x')
    f = function_trig_fx(x)
    fprime = sym.diff(f, x)
    return fprime.evalf(subs={x: x0})

def compute_Sf_x(d_a,x_i,y_i,not_x):
    A = [d_a]
    h = []

    for i in range(len(y_i)-1):
        h.append(x_i[i+1]-x_i[i])
        A_aux = -A[i] + (2*(y_i[i+1]-y_i[i]))/h[i]
        A.append(A_aux)

    for item in range(len(x_i)):
        if (x_i[item] < not_x):
            x_i1 = x_i[item]
            i_X = item
            x_i2 = x_i[item + 1]
    print("Vectorul A:",A)
    print("Vectorul h:", h)
    Sf_x = ((A[i_X+1]-A[i_X])/(2*h[i_X]))*pow(not_x-x_i1,2) + A[i_X]*(not_x-x_i1) + y_i[i_X]
    return Sf_x







def workspace():
    #Polynomial approximation
    x0 = int(input("enter x0:"))
    xn = int(input("enter xn:"))
    print(x0, xn)
    xi = generate_xi_values(x0, xn)
    yi = generate_yi_values(xi)
    matrix_b = compute_matrix_b(xi)

    #linear system Ba = f => ai
    ai = compute_ai(matrix_b, yi)

    #compute Pm(x) Horner schema
    Pm_x = compute_Pm_not_x(ai, 3.0)
    print("Pm_x = ",Pm_x)
    print("|Pm(x)-f(x)|", abs(Pm_x-function_fx(3.0)))
    sum = 0
    for i in range(len(xi)):
        Pm_x2 = compute_Pm_not_x(ai, xi[i])
        sum = sum + abs(Pm_x2-yi[i])
    print("Sum ABS : ", sum)


    # Trigonometric approximation
    print("\n\nAproximare trigonometrica")
    x0_t = float(input("enter x0_t:"))
    xn_t = float(input("enter xn_t:"))
    t_xi = generate_xi_values(x0_t, xn_t)
    t_yi = generate_yi_trigonometric_values(t_xi)

    d_a = derivata(x0_t)

    Sf_x = compute_Sf_x(d_a, t_xi, t_yi, 1.2)
    print("Sf_x = ", Sf_x)
    print("|Sf(x)-f(x)| = ", abs(Sf_x-function_trig_fx(1.2)))


    # Bonus
    plot_f()
    plot_Pm(ai)
    aii_vec=[]
    for i in np.arange (start=0.1, stop=1.5, step=0.2):
        aii_vec.append(compute_Sf_x(d_a, t_xi, t_yi, i))
    plot_Sf(aii_vec)


# workspace()