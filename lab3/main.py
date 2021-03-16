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



a = citire_eficienta_a("res/b.txt")
print(a)
