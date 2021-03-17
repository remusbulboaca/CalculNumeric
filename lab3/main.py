import numpy as np
from copy import copy, deepcopy
epsilon = 10 ** float(-16)

class matriceA:
    a = []
    def citire_eficienta_a(self,filename):
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
    def citire_eficienta_b(self,filename):
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
                if(line == '\n'):
                    switch = switch + 1
                    continue
                if(switch == 0):
                    a.append(float(line.rstrip('\n')))
                if(switch == 1):
                    b.append(float(line.rstrip('\n')))
                if(switch == 2):
                    c.append(float(line.rstrip('\n')))
        self.a = a
        self.b = b
        self.c = c
        self.p = p
        self.q = q
class Matrix_operations:
    sum = []
    def sum(self,matriceB, matriceA):
        acopy = [row[:] for row in matriceA.a]

        p = matriceB.p
        q = matriceB.q
        # for i in range(0,len(acopy)):
        #     for values in acopy[i]:
        
        # line = linie
        # j[0] = valoare 
        # j[1] = coloana
        
        for line,sub_list in enumerate(acopy):
            for index,j in enumerate(sub_list):
                if(j[1] == line):
                    acopy[line][index] = (j[0] + matriceB.a[line],j[1])
                if(j[1]-line == q):
                    acopy[line][index] = (j[0] + matriceB.b[line],j[1])
                if(line-j[1] == p):
                    acopy[line][index] = (j[0] + matriceB.c[j[1]],j[1])
        self.sum = acopy
        
    def multiply(self,matriceA,matriceB):
        sumcopy = [row[:] for row in matriceA.a]
        q = matriceB.q
        p = matriceB.p
        # for line,sub_list in enumerate(matriceA.a):
        #     for index,j in enumerate(sub_list):
        #         if(line == 0):
        #             sumcopy[line][index] = (j[0] * matriceB.a[j[1]] , j[1])
        #             sumcopy[line][index] = sumcopy[line][2] * matriceB.c[0]

        #         # if(line>0 and line < len(matriceA.a)):    
        #         #     #

        #         # if(line == len(matriceA.a)):
        #         #     #
        
        for line,sub_list in enumerate(sumcopy):
            for index,j in enumerate(sub_list):
                if(j[1] == line):
                    sumcopy[line][index] = (j[0] * matriceB.a[j[1]],j[1])
                if(j[1]-line == q):
                    sumcopy[line][index] = (j[0] * matriceB.b[j[1]-q+1],j[1])
                if(line-j[1] == p):
                    sumcopy[line][index] = (j[0] * matriceB.c[j[1]-p],j[1])

        return sumcopy

    def compare_vectors(self,a,b):
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

    # def inmultesteMatrici(a, b):
    # mat = []
    # for i in range(len(a)):
    #     linie = []
    #     for j in range(len(b)):
    #         sum = 0
    #         for l in range(len(a[i])):
    #             bb = 0
    #             for x in range(len(b[a[i][l][1]])):
    #                 if b[a[i][l][1]][x][1] == j % (len(b)):
    #                     bb = b[a[i][l][1]][x][0]
    #                     break

    #             sum = sum + bb * a[i][l][0]
    #         if sum != 0:
    #             linie.append([sum, j])
    #     mat.append(linie)

    # return mat       


a = matriceA
a.citire_eficienta_a(a,"res/a.txt")

b = matriceB
b.citire_eficienta_b(b,"res/b.txt")

operations = Matrix_operations()
operations.sum(b,a)

aplusb = matriceA
aplusb.citire_eficienta_a(aplusb,"res/aplusb.txt")
#print(operations.sum[2020])
aorib = matriceA
aorib.citire_eficienta_a(aorib,"res/aorib.txt")

print(operations.compare_vectors(aplusb.a,a.a))

#----------------------------------------------------------------

anew = matriceA
anew.citire_eficienta_a(anew,"res/a.txt")
# print(anew.a[0])
# print(b.a[0])
# print(b.c[0])
# print(b.b[0])
# print(anew.a[1])
print(aorib.a[0])
print(operations.multiply(anew,b)[0])


