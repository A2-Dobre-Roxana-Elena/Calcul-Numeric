import numpy as np
import math


def citimBsiN():
    f = open("b1.txt.txt", "r")
    b = []
    n = int(f.readline())
    for linie in f:
        b.append(float(linie))
    f.close()
    return b, n


def citimMatriceRara():
    f = open("a1.txt.txt", "r")
    n = int(f.readline())
    matriceRara = []
    for i in range(n):
        matriceRara.append([])

    # facem parsarea
    for linie in f.readlines():
        if len(linie.split(',')) > 2:
            linie = linie.strip('\n').replace(' ', '')
            tupla = linie.split(',')
            valoare = float(tupla[0])
            i = int(tupla[1])
            j = int(tupla[2])

            # aici verficam daca elementele de pe diagonala principala sunt nenule
            if i == j and np.abs(valoare) < epsilon:
                return exit(0)

            # aici verificam daca avem duplicate, daca avem, elementele primesc suma duplicatelor
            valoareExistenta = False
            for x in matriceRara[i]:
                if x[1] == j:
                    x[0] += valoare

            element = (valoare, j)
            matriceRara[i].append(element)
    f.close()
    return matriceRara


def GaussSeidel(_rare_matrix, _x, _b, eps):
    while True:
        suma = 0
        for i in range(len(_x)):
            # the sum of the products from line A and column matrix b
            product_sum = 0

            for _tuple in _rare_matrix[i]:
                # landed on a diagonal element
                if i == _tuple[1]:
                    diagonal_value = _tuple[0]
                else:
                    product_sum += _tuple[0] * _x[_tuple[1]]

            #aici e vechiul element!!!
            #conform formulei, enoul element minus  vechiul element  !!!
            suma += (float((_b[i] - product_sum) / diagonal_value) - _x[i]) * (
                    float((_b[i] - product_sum) / diagonal_value) - _x[i])

            #updatam vectorul x
            _x[i] = float((_b[i] - product_sum) / diagonal_value)

        #norma e calculata ca radical din patratul fiecarui element, conform formulei
        norm = math.sqrt(suma)
        #ultima verificare
        if norm < eps:
            return _x


def norma_infinita(A, x, b):
    #norma = cea mai mare valoarea absoluta a elementelor
    max = 0
    for i in range(len(A)):
        sum = 0
        for tuple in A[i]:
            #aici e inmultirea intre matrici si vector
            sum += tuple[0] * x[tuple[1]]
        if abs(sum - b[i]) > max: #asta se cere, a*x - b
            max = abs(sum - b[i])
    return max


if __name__ == '__main__':
    # ex1
    epsilon = pow(10, -8)
    b, n = citimBsiN()
    matriceRara = citimMatriceRara()
    # ex2
    x = np.zeros(n)
    x = GaussSeidel(matriceRara, x, b, epsilon)
    print(x)

    print("A*x_GS - b = ", norma_infinita(matriceRara, x, b))