import random
from contextlib import redirect_stdout
from scripts import *
from scipy.linalg import lu
import json
import sys

#Ex1:
# initiala

def main(filename,mode,len):


    stdoutOrigin = sys.stdout
    sys.stdout = open("out.txt", "w")

    def load_input(file_name=filename):
        with open(file_name, 'r') as file_handler:
            return json.load(file_handler)

    if mode == "File":
        data = load_input()

        A = np.array(data[0])
        b = np.array(data[1])
        m = np.array(data[2])

    if mode == "Generate":
        m = 18

        b1 = np.random.random_integers(0, 5, size=(int(len), int(len)))
        A = (b1 + b1.T) / 2
        # A = np.array([[2.25, 3, 3],[3, 9.0625, 13],[3, 13, 24]])


        # b = np.array([9, 35.0625, 61])
        b = np.random.random_integers(1, 3,size = (int(len)))

        print("\nA: \n",A)
        print("\nb: \n", b)


    epsilon = 10**float(-m)




    print("\nEpsilon: ",epsilon)

    if verify_matrix(A):
        print("\nA: \n", A)
        print("\nb: \n", b)
        # descompunerea L
        L = cholesky(A)
        print("\nL:\n",L)
        # L transpusa
        Lt = transpusa(L)
        print("Lt : \n",Lt)


        #Ex2:
        print("-"*20)
        print("\n Ex2: \n")
        print("Det A: ", determinant(L)*determinant(Lt))

        #Ex3:
        print("-" * 20)
        print("\n Ex3: \n")
        x = np.array([])
        x = np.append(x, solve_system(L,b,x,epsilon))
        print(x)

        #Ex4:
        print("-" * 20)
        print("\n Ex4: \n")
        solution_check(A,x,b)

        #Ex5:
        print("-" * 20)
        print("Ex5:")
        p, l, u = lu(A)
        print("\nL:\n",l, "\n")
        print("\nU:\n",u, "\n")
        x1 = np.linalg.solve(A, b)
        print("\nx:\n",x1)

        #Ex6:
        print("-" * 20)
        print("\nEx6:")
        print("\nLLt:\n",invert_matrix(LLt_generate(L,Lt),epsilon), "\n")
        print("\nLLt_numpy:\n",np.linalg.inv(LLt_generate(L,Lt)), "\n")
        print("\nLLt-LLt_numpy:\n",np.linalg.norm(invert_matrix(LLt_generate(L,Lt),epsilon) - LLt_generate(L,Lt)), "\n")
    else:
        print("Matricea nu este pozitiva")

    sys.stdout.close()
    sys.stdout=stdoutOrigin

    with open('out.txt', 'r') as f:
        print(f.read())
