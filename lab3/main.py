import numpy as np
from copy import copy, deepcopy

epsilon = 10 ** float(-16)

class matriceA:
    a = []

    def citire_eficienta_a(self, filename):
        with open(filename, 'r') as f:
            n = f.readline()
            a = [[] for i in range(int(n))]
            for line in f:
                if line == '\n':
                    continue
                elements = line.split(', ')
                val = float(elements[0])
                i = int(elements[1])
                j = int(elements[2])
                # daca exista vloarea deja se aduna
                already = False
                for index, sub_list in enumerate(a[i]):
                    if sub_list[1] == j:
                        a[i][index] = (sub_list[0] + val, sub_list[1])
                        already = True

                if not already:
                    a[i].append((val, j))
            self.a = a

class matriceB:
    a = []
    b = []
    c = []
    p = None
    q = None

    def citire_eficienta_b(self, filename):
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
        self.a = a
        self.b = b
        self.c = c
        self.p = p
        self.q = q

class Matrix_operations:
    sum = []
    prod = []

    def sum(self, matriceB, matriceA):
        acopy = [row[:] for row in matriceA.a]

        p = matriceB.p
        q = matriceB.q
        # for i in range(0,len(acopy)):
        #     for values in acopy[i]:

        # line = linie
        # j[0] = valoare
        # j[1] = coloana

        for line, sub_list in enumerate(acopy):
            for index, j in enumerate(sub_list):
                if (j[1] == line):
                    acopy[line][index] = (j[0] + matriceB.a[line], j[1])
                if (j[1] - line == q):
                    acopy[line][index] = (j[0] + matriceB.b[line], j[1])
                if (line - j[1] == p):
                    acopy[line][index] = (j[0] + matriceB.c[j[1]], j[1])
        self.sum = acopy

    def multiply(self, matriceA, matriceB):
        sumcopy = [row[:] for row in matriceA.a]
        q = matriceB.q
        p = matriceB.p


        for line, sub_list in enumerate(sumcopy):
            for index, j in enumerate(sub_list):
                if (j[1] == line):
                    sumcopy[line][index] = (j[0] * matriceB.a[j[1]], j[1])
                if (j[1] - line == q):
                    sumcopy[line][index] = (j[0] * matriceB.b[j[1] - q + 1], j[1])
                if (line - j[1] == p):
                    sumcopy[line][index] = (j[0] * matriceB.c[line - p], j[1])

        self.sum = sumcopy

    def compare_vectors(self, a, b):
        for line_num, i in enumerate(a):
            for j in i:
                not_found = True
                for tup in b[line_num]:
                    if tup[1] == j[1]:
                        if abs(tup[0] - j[0]) < epsilon:
                            not_found = False
                            break
                if not_found:
                    return False
        return True

def verificare_adunare_main(matrixB,matrixA):
    operations = Matrix_operations()
    operations.sum(matrixB, matrixA)
    aplusb = matriceA
    aplusb.citire_eficienta_a(aplusb, "res/aplusb.txt")
    return operations.compare_vectors(aplusb.a, matrixA.a)

def verificare_inmultire_main(matrixB):
    a1 = matriceA
    a1.citire_eficienta_a(a1, "res/a.txt")

    aorib = matriceA
    aorib.citire_eficienta_a(aorib, "res/aorib.txt")

    operations = Matrix_operations()
    operations.multiply(a1,matrixB)

    return operations.compare_vectors(aorib.a, a1.a)


# a = matriceA
# a.citire_eficienta_a(a, "res/a.txt")
#
# b = matriceB
# b.citire_eficienta_b(b, "res/b.txt")
#
#
# # # ----------------------------------------------------------------
# # Adunare
# print("\nAdunare:")
#
# print(verificare_adunare_main(b,a))
#
# # operations = Matrix_operations()
# # operations.sum(b, a)
# #
# # aplusb = matriceA
# # aplusb.citire_eficienta_a(aplusb, "res/aplusb.txt")
# # print(operations.compare_vectors(aplusb.a, a.a))
# # print("\n")
#
# # # ----------------------------------------------------------------
# # Inmultire
#
# print("Inmultire: ")
# # a1 = matriceA
# # a1.citire_eficienta_a(a1, "res/a.txt")
# #
# # aorib = matriceA
# # aorib.citire_eficienta_a(aorib, "res/aorib.txt")
# #
# # operations = Matrix_operations()
# # operations.multiply(a1,b)
# # # print(a1.a[1])
# # # print(aorib.a[1])
# # print(operations.compare_vectors(aorib.a, a1.a))
# # print("\n")
#
# print(verificare_inmultire_main(b))
