from pprint import pprint
from scripts import *

# initiala
A = np.array([[2.25, 3, 3], [3, 9.0625, 13], [3, 13, 24]])
# descompunerea L
L = cholesky(A)
print(L)
# L transpusa
Lt = transpusa(L)

# determinant A
detA = determinant(L)*determinant(Lt)  
print("Determinant L*Lt L:", detA)

