import numpy as np

def citire_eficienta_a(filename):
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
            #daca exista vloarea deja se aduna
            already = False
            for index, sub_list in enumerate(a[i]):
                if sub_list[1] == j:
                    a[i][index] = (sub_list[0] + val, sub_list[1])
                    already = True

            if not already:
                a[i].append((val, j))
        return a

def citire_eficienta_b(filename):
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
                a.append(line.rstrip('\n'))
            if(switch == 1):
                b.append(line.rstrip('\n'))
            if(switch == 2):
                c.append(line.rstrip('\n'))     
    print(len(a),len(b),len(c))
# a = citire_eficienta_a("res/a.txt")
citire_eficienta_b("res/b.txt")
