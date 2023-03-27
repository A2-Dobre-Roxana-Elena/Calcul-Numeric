import math
import random

from matplotlib import pyplot as plt
import numpy as np


# creaza matricea random - ex6
def creareMatrice(dimensiune):
    matrice = np.array([[0 for i in range(dimensiune)] for j in range(dimensiune)], dtype='f')
    for i in range(0, dimensiune):
        for j in range(0, dimensiune):
            if i >= j:
                matrice[i][j] = matrice[j][i] = random.randint(0, 5)
    return matrice


# creaza vectorul s random -ex6
def creareS(dimensiune):
    vector = np.array([0 for j in range(dimensiune)], dtype='f')
    for i in range(0, dimensiune):
        # vector[i] = round(random.uniform(0.0, 50.0), 2)
        vector[i] = random.randint(0, 50)
    return vector


# ex1-calcul b
def calculB(A, s):
    b = np.zeros(n)
    for i in range(n):
        for j in range(n):
            b[i] = b[i] + s[j] * A[i][j]
    return b


# ex2-algoritmul Householder
def algoritmulHouseHolder(A, b, n):
    Q_initial = np.identity(n)
    #print(Q_initial)
    u = np.zeros(n)
    for r in range(n - 1):
        theta = 0.0
        for i in range(r, n):
            theta = theta + A[i][r] * A[i][r]
        if theta < eps:
            break
        k = np.sqrt(theta)
        if A[r][r] > 0:
            k = -k
        beta = theta - k * A[r][r]
        u[r] = A[r][r] - k
        for i in range(r + 1, n):
            u[i] = A[i][r]

        # A=Pr*A
        # tranformarea coloanelor j = r + 1, ..., n
        for j in range(r + 1, n):
            gama_nou = 0.0
            for i in range(r, n):
                gama_nou = gama_nou + u[i] * A[i][j]
            gama = gama_nou / beta
            for i in range(r, n):
                A[i][j] = A[i][j] - gama * u[i]
        # transformarea coloanei r a matricei A
        A[r][r] = k
        for i in range(r + 1, n):
            A[i][r] = 0

        # b = Pr*b
        gama_nou = 0.0
        for i in range(r, n):
            gama_nou = gama_nou + u[i] * b[i]
        gama = gama_nou / beta
        for i in range(r, n):
            b[i] = b[i] - gama * u[i]

        # Q_initial = Pr*Q_initial

        for j in range(n):
            gama_nou = 0.0
            for i in range(r, n):
                gama_nou = gama_nou + u[i] * Q_initial[i][j]
            gama = gama_nou / beta
            for i in range(r, n):
                Q_initial[i][j] = Q_initial[i][j] - gama * u[i]

    return Q_initial, A, b


# ------------------------------------------------------------
print("Exercitiul 1")
# print("Introduceti dimensiunea matricei: ")
# n = int(input())

# ex6 matrice random si vector s random
# A_initial = creareMatrice(n)
# print("Matricea: ")
# print(A)
#
# s = creareS(n)
# print("Vectorul s: ", s)


# exemplul din notite
n = 3
m = 8
eps = 10 ** -m

A_initial = np.array([[0, 0, 4], [1, 2, 3], [0, 1, 2]])
s = np.array([3, 2, 1])

# ex1
b_initial = calculB(A_initial, s)
print("Vectorul b:", b_initial)

# ex2
AH = A_initial.copy()
bH = b_initial.copy()
print("Exercitiul 2")
Q, AH, bH = algoritmulHouseHolder(AH, bH, n)
Q = Q.T
print('Q Householder:')
print(Q)
print("R Householder:")
print(AH)

# ex3
print("Exercitiul 3")
x_Householder = np.linalg.solve(AH, bH)
Q_numpy, R_numpy = np.linalg.qr(A_initial)
x_QR = np.linalg.solve(R_numpy, np.dot(Q_numpy.T, b_initial))
print("Householder:")
print(x_Householder)
print("Descompunerea QR:")
print(x_QR)
print("Norma:")
print(np.linalg.norm(x_QR - x_Householder))

# ex4
print("Exercitiul 4")
print("Norma (A_initial x_Householder - b_initial):")
print(np.linalg.norm(A_initial @ x_Householder - b_initial))

print("Norma (A_initial x_QR - b_initial):")
print(np.linalg.norm(A_initial @ x_QR - b_initial))

print("Norma (x_Householder - s)/ Norma (s):")
print(np.linalg.norm(x_Householder - s) / np.linalg.norm(s))

print("Norma (x_QR - s)/ Norma (s):")
print(np.linalg.norm(x_QR - s) / np.linalg.norm(s))

# ex5
print("Exercitiul 5")
# am calculat descompunerea QR cu algoritmul Householder
# verificam daca e singulara
for i in range(n):
    if math.fabs(AH[i][i]) < eps:
        print('Inversa matricei A nu se poate calcula')
        exit(1)
# se poate calcula inversa, calculam coloanele
A_inversa = np.zeros((n, n))
for j in range(n):
    b = np.zeros(n)
    for i in range(n):
        b[i] = Q.T[i][j]
    # se rezolva sis superior triunghilar R*x=b
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = 0.0
        for k in range(i + 1, n):
            suma += AH[i][k] * x[k]
        x[i] = (b[i] - suma) / AH[i][i]
    for i in range(0, n):
        A_inversa[i][j] = x[i]
print(A_inversa)

# bonus
print("Bonus")
A_simetric = np.array([[0, 0, 4],
                      [0, 1, 2],
                      [4, 2, 3]])
# A_simetric = creareMatrice(3)
print(A_simetric)
for k in range(0, 1000):
    b = np.zeros(n)
    # print(b)
    Q, R, b = algoritmulHouseHolder(A_simetric, b, n)
    Q = Q.T

    Ak = Q @ R
    Ak1 = R @ Q
    # print(Ak)
    # print(Ak1)

    norma = np.linalg.norm(Ak1 - Ak)
    if norma <= eps:
        print("Norma este: ")
        print(norma)
        print("A(k+1):")
        print(Ak1)
        break
    A_simetric = Ak1
