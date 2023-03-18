import numpy as np
import scipy.linalg
import random


def eSimetrica(matrice):
    return np.allclose(matrice, matrice.T)


def creareMatrice(dimensiune):
    matrice = np.array([[0 for i in range(dimensiune)] for j in range(dimensiune)], dtype='f')
    for i in range(0, dimensiune):
        for j in range(0, dimensiune):
            if i >= j:
                # matrice[i][j] = matrice[j][i] = round(random.uniform(0.0, 50.0), 2)
                matrice[i][j] = matrice[j][i] = random.randint(0, 50)
    for i in range(0, dimensiune):
        sum = 0
        for j in range(0, dimensiune):
            if i != j:
                sum += abs(matrice[i][j])
        matrice[i][i] = sum
    return matrice


def creareB(dimensiune):
    vector = np.array([0 for j in range(dimensiune)], dtype='f')
    for i in range(0, dimensiune):
        # vector[i] = round(random.uniform(0.0, 50.0), 2)
        vector[i] = random.randint(0, 50)
    return vector


def descompunereCholenski(A):
    n = A.shape[0]
    D = np.zeros(n)
    for p in range(n):
        sum = 0.0
        # formula 9
        for j in range(p):
            sum += D[j] * A[p][j] * A[p][j]
        D[p] = A[p][p] - sum

        # formula 10
        for i in range(p, n):
            sum = 0.0
            for j in range(p):
                sum += D[j] * A[i][j] * A[p][j]
            if (abs(D[p]) < epsilon):
                print("EROARE: Impartire la 0.")
                exit(1)
            else:
                res = (A[p][i] - sum) / D[p]
                A[i][p] = float(res)
    return A, D


def gasimPeX(matrix, b, n, D):
    # metoda substitutiei directe:
    # aflam z: L*z = b
    z = np.zeros(n, dtype='f')
    for i in range(n):
        sum = 0.0
        for j in range(i):
            sum += A[i][j] * z[j]
        z[i] = b[i] - sum

    # aflam y: yi=z[i]/D[i]
    y = np.zeros(n, dtype='f')
    for i in range(n):
        y[i] = z[i] / D[i]
    print("This is y: ")
    print(y)

    # aflam x - metoda substitutiei inverse
    # Lt*x = y
    x = np.zeros(n, dtype='f')
    for i in range(n - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum += A.T[i][j] * x[j]
        x[i] = y[i] - sum

    return x, y, z

"""
A = np.array([[1, 1, 3],
              [1, 1, 15.5],
              [3, 15.5, 43]], dtype='f')"""

epsilon = pow(10, -6)

print("Introduceti dimensiunea matricei: ")
n = int(input())

A = creareMatrice(n)
Ainit = A.copy()

# b = np.array([12, 38, 68], dtype="f")
b = creareB(n)

print("Matricea A este egal cu ", A)
# print(n)
print("---------")
print("Vectroul B este egal cu ", b)
print("---------")

A, D = descompunereCholenski(A)

print("EX 1")
print("Matricea A dupa descompunerea Choleski este ", A)
print("---------")
print("Matricea D este egala cu ", D)

print("EX 3")
x, y, z = gasimPeX(A, b, A.shape[0], D)
x_chol = x.copy()
print("X-ul este egal cu : \n", x)

print("EX 2")
# Calculam determinantul -> det A = detD
print(f'det(A) = {np.prod(D)}')

print("EX 4")
# Calculam A = LU folosinf libraria
P, L, U = scipy.linalg.lu(A)
print("L este egal cu :")
print(L)

print("U este egal cu :")

print(U)

# Calculam Ax = b
x = np.linalg.solve(Ainit, b)
if np.allclose(np.dot(Ainit, x), b):
    print(f'Solutia x pentru Ax = b este ::\n{x}')
else:
    print(f'Eroare Ax = b.\n')
    # exit(4)

print("EX 5")
# Verificam daca A_init * x_chol - b < eps
eps = 10 ** (-5)
if np.linalg.norm(Ainit @ x_chol - b) < eps:
    print(f'LDLT a fost calculat corespunzator')
else:
    print(f'LDLT nu a fost calculat corespunzator')
    # exit(5)

# BONUS

# return numpy.allclose(REZ, A_copy, rtol=eps, atol=eps)
# partea inferioara a lui A
REZ = np.tril(A) @ np.diag(D) @ np.tril(A).T  # inmultim cele trei matrici
print(f'REZ = {REZ}')
if np.allclose(REZ, Ainit, rtol=eps, atol=eps):  # verificam egalitatea
    print(f'Bonusul este bun\n')
else:
    print(f'Bonusul nu este bun\n')
