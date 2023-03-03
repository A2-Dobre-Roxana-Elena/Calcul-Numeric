# exercitiul 1
import math

m = 0
u = 10 ** (-m)

while 1 + u != 1 and u > 0:
    m = m + 1
    u = 10 ** (-m)

m = m - 1
u = 10 ** (-m)
print("Precizia masina este : ", u, ", m-ul fiind egal cu ", m)

# exercitiul 2

x = 1.0
y = u
z = u

if (x + y) + z != x + (y + z):
    print("Adunare este neasociativa")
else:
    print("Adunare este asociativa")

# inmultire neasociativa
import time
import random

start = time.time_ns()
contor = 1
x = round(random.uniform(1, 5), 15)
y = round(random.uniform(1, 5), 15)
z = round(random.uniform(1, 5), 15)

while (x * y) * z == x * (y * z):
    contor += 1
    x = round(random.uniform(1, 5), 15)
    y = round(random.uniform(1, 5), 15)
    z = round(random.uniform(1, 5), 15)

finish = time.time_ns()
runningTime = finish - start
# print(start)
# print(finish)
print(" Inmultirea nu este asociativa, deoarece s-a gasit exempul numerelor: x= ", x, ", y= ", y, ",z= ", z)
print(" Numerele s-au gasit in ", contor, f"incercari, avand un timp de rulare al programului egal cu {runningTime}")


# exercitiul 3
def adunareMatrici(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]  # initilizeaza cu 0 matricea c n x n
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]  # adunare pentru fiecare pozitie
    return C


def scadereMatrici(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]  # initilizeaza cu 0 matricea c n x n
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]  # scadere pentru fiecare pozitie
    return C


def inmultireClasicaMatrici(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]  # initilizeaza cu 0 matricea c n x n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]  # inmultirea clasica cu suma
    return C


def Strassen(A, B, n, n_min):
    # pentru n <= n_min, se foloseste metoda de inmultire clasica a matricilor
    if n <= n_min:
        return inmultireClasicaMatrici(A, B, n)

    # facem split la matricele de intrare A pentru a le folosi la calculul P-urilor
    m = n // 2
    A11 = [[A[i][j] for j in range(m)] for i in range(m)]
    A12 = [[A[i][j + m] for j in range(m)] for i in range(m)]
    A21 = [[A[i + m][j] for j in range(m)] for i in range(m)]
    A22 = [[A[i + m][j + m] for j in range(m)] for i in range(m)]

    # facem split la matricele de intrare B pentru a le folosi la calculul P-urilor
    B11 = [[B[i][j] for j in range(m)] for i in range(m)]
    B12 = [[B[i][j + m] for j in range(m)] for i in range(m)]
    B21 = [[B[i + m][j] for j in range(m)] for i in range(m)]
    B22 = [[B[i + m][j + m] for j in range(m)] for i in range(m)]

    # calculam P-urile
    P1 = Strassen(adunareMatrici(A11, A22, m), adunareMatrici(B11, B22, m), m, n_min)
    P2 = Strassen(adunareMatrici(A21, A22, m), B11, m, n_min)
    P3 = Strassen(A11, scadereMatrici(B12, B22, m), m, n_min)
    P4 = Strassen(A22, scadereMatrici(B21, B11, m), m, n_min)
    P5 = Strassen(adunareMatrici(A11, A12, m), B22, m, n_min)
    P6 = Strassen(scadereMatrici(A21, A11, m), adunareMatrici(B11, B12, m), m, n_min)
    P7 = Strassen(scadereMatrici(A12, A22, m), adunareMatrici(B21, B22, m), m, n_min)

    # calculam C-urile
    C11 = adunareMatrici(scadereMatrici(adunareMatrici(P1, P4, m), P5, m), P7, m)
    C12 = adunareMatrici(P3, P5, m)
    C21 = adunareMatrici(P2, P4, m)
    C22 = adunareMatrici(scadereMatrici(adunareMatrici(P1, P3, m), P2, m), P6, m)

    # construim matricea rezultat C din imbinarea c11, c12, c21, c22
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j + m] = C12[i][j]
            C[i + m][j] = C21[i][j]
            C[i + m][j + m] = C22[i][j]

    return C


A = [[4, 1, 2, 4, 1, 2, 3, 4], [7, 5, 3, 4, 1, 2, 3, 4], [9, 6, 9, 4, 1, 2, 3, 4], [2, 3, 4, 4, 1, 2, 3, 4],
     [4, 1, 2, 4, 1, 2, 3, 4], [7, 5, 3, 4, 1, 2, 3, 4], [9, 6, 9, 4, 1, 2, 3, 4], [2, 3, 4, 4, 1, 2, 3, 4]]
B = [[4, 1, 2, 4, 1, 2, 3, 4], [7, 5, 3, 4, 1, 2, 3, 4], [9, 6, 9, 4, 1, 2, 3, 4], [2, 3, 4, 4, 1, 2, 3, 4],
     [4, 1, 2, 4, 1, 2, 3, 4], [7, 5, 3, 4, 1, 2, 3, 4], [9, 6, 9, 4, 1, 2, 3, 4], [2, 3, 4, 4, 1, 2, 3, 4]]
n = 8
nminim = 2

matrix = Strassen(A, B, n, nminim)
result=inmultireClasicaMatrici(A,B,n)

for i in result:
    print(i)
print("Strassen")
for i in matrix:
    print(i)




#bonus
def adunareMatrici(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]  # initilizeaza cu 0 matricea c n x n
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]  # adunare pentru fiecare pozitie
    return C


def scadereMatrici(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]  # initilizeaza cu 0 matricea c n x n
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]  # scadere pentru fiecare pozitie
    return C


def inmultireClasicaMatrici(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]  # initilizeaza cu 0 matricea c n x n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]  # inmultirea clasica cu suma
    return C


def Strassen(A, B, n, n_min):
    # verificam daca n = 2**q, daca nu este o formam adaugand linii si coloane cu 0
    randuriSuplimetare = 0
    i = math.log2(n)
    #print(i)
    #print(int(i))
    while i != int(i):
        n += 1
        randuriSuplimetare += 1
        #print(n)
        X = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - randuriSuplimetare):
            for j in range(n - randuriSuplimetare):
                X[i][j] = A[i][j]
        Y = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - randuriSuplimetare):
            for j in range(n - randuriSuplimetare):
                Y[i][j] = B[i][j]
        A = X
        B = Y
        i = math.log2(n)

    # pentru n <= n_min, se foloseste metoda de inmultire clasica a matricilor
    if n <= n_min:
        return inmultireClasicaMatrici(A, B, n)

    # facem split la matricele de intrare A pentru a le folosi la calculul P-urilor
    m = n // 2
    A11 = [[A[i][j] for j in range(m)] for i in range(m)]
    A12 = [[A[i][j + m] for j in range(m)] for i in range(m)]
    A21 = [[A[i + m][j] for j in range(m)] for i in range(m)]
    A22 = [[A[i + m][j + m] for j in range(m)] for i in range(m)]

    # facem split la matricele de intrare B pentru a le folosi la calculul P-urilor
    B11 = [[B[i][j] for j in range(m)] for i in range(m)]
    B12 = [[B[i][j + m] for j in range(m)] for i in range(m)]
    B21 = [[B[i + m][j] for j in range(m)] for i in range(m)]
    B22 = [[B[i + m][j + m] for j in range(m)] for i in range(m)]

    # calculam P-urile
    P1 = Strassen(adunareMatrici(A11, A22, m), adunareMatrici(B11, B22, m), m, n_min)
    P2 = Strassen(adunareMatrici(A21, A22, m), B11, m, n_min)
    P3 = Strassen(A11, scadereMatrici(B12, B22, m), m, n_min)
    P4 = Strassen(A22, scadereMatrici(B21, B11, m), m, n_min)
    P5 = Strassen(adunareMatrici(A11, A12, m), B22, m, n_min)
    P6 = Strassen(scadereMatrici(A21, A11, m), adunareMatrici(B11, B12, m), m, n_min)
    P7 = Strassen(scadereMatrici(A12, A22, m), adunareMatrici(B21, B22, m), m, n_min)

    # calculam C-urile
    C11 = adunareMatrici(scadereMatrici(adunareMatrici(P1, P4, m), P5, m), P7, m)
    C12 = adunareMatrici(P3, P5, m)
    C21 = adunareMatrici(P2, P4, m)
    C22 = adunareMatrici(scadereMatrici(adunareMatrici(P1, P3, m), P2, m), P6, m)

    # construim matricea rezultat C din imbinarea c11, c12, c21, c22
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j + m] = C12[i][j]
            C[i + m][j] = C21[i][j]
            C[i + m][j + m] = C22[i][j]

    # stergem randurile suplimentare
    if randuriSuplimetare != 0:
        X = [[0 for i in range(n - randuriSuplimetare)] for j in range(n - randuriSuplimetare)]
        for i in range(n - randuriSuplimetare):
            for j in range(n - randuriSuplimetare):
                X[i][j] = C[i][j]
        C = X

    return C


AB = [[4, 1, 2, 4, 1, 2, 3], [7, 5, 3, 4, 1, 2, 3], [9, 6, 9, 4, 1, 2, 3], [2, 3, 4, 4, 1, 2, 3],
     [4, 1, 2, 4, 1, 2, 3], [7, 5, 3, 4, 1, 2, 3], [9, 6, 9, 4, 1, 2, 3]]
BB = [[4, 1, 2, 4, 1, 2, 3], [7, 5, 3, 4, 1, 2, 3], [9, 6, 9, 4, 1, 2, 3], [2, 3, 4, 4, 1, 2, 3],
     [4, 1, 2, 4, 1, 2, 3], [7, 5, 3, 4, 1, 2, 3], [9, 6, 9, 4, 1, 2, 3]]
nB = 7
nminimB = 2

matrix = Strassen(AB, BB, nB, nminimB)
print("Inmultirea a doua matrici de dimensiuni oarecare:")
for i in matrix:
    print(i)