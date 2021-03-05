from pprint import pprint
from scripts import *
import scipy
import json

#Ex1:
# initiala
def load_input(file_name=r'data.json'):
    with open(file_name, 'r') as file_handler:
        return json.load(file_handler)
data = load_input()

A = np.array(data[0])
b = np.array(data[1])

# descompunerea L
L = cholesky(A)
print("L:\n",L)
# L transpusa
Lt = transpusa(L)
print("Lt : \n",Lt)

#Ex2:
print("\nDet A: ", determinant(L)*determinant(Lt))

#Ex3:
x = np.array([])
solve_system(L,b,x)
