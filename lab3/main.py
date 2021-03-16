import numpy as np


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
        acopy = matriceA.a
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
        
        


a = matriceA
a.citire_eficienta_a(a,"res/a.txt")

b = matriceB
b.citire_eficienta_b(b,"res/b.txt")


operations = Matrix_operations()
operations.sum(b,a)
print(operations.sum)





