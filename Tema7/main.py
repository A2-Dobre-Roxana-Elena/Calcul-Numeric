import numpy as np
import random
import math

epsilon = pow(10,-8)


def citireaPolinomului():
    lst = []
    n = int(input("Introduceti numarul de coeficienti : "))
    print("Introduceti coeficientii : ")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    return np.poly1d(lst), lst


def Horner( listaCoeficienti, x):
    bAnterior = listaCoeficienti[0]
    for i in range (1, len(listaCoeficienti)+1):
        bCurent = listaCoeficienti[i] + bAnterior * x
        bAnterior = bCurent
    return bCurent


def Semn ( valoare):
    if valoare < 0:
        return -1
    return 1


def calcH(n, p, pd, pdd):
    return (n - 1) ** 2 * (pd ** 2) - n * (n - 1) * p * pdd


def metodaLuiLaguerre(listaCoeficienti, R, kMax):
    # x0 == x, x1 == y...
    x = random.uniform(-R, R)
    #print(x)
    # ne pregatim de Horner

    valPolinomInX = Horner(listaCoeficienti,x)
    polinom = np.poly1d(listaCoeficienti)
    derivataI = polinom.deriv(1)
    coefDerivataI = derivataI.coef

    valDerivataI = Horner(coefDerivataI, x)
    semn = Semn(valDerivataI)

    derivataII = derivataI.deriv(1)
    coefDerivataII = derivataII.coef
    valDerivataII = Horner(coefDerivataII, x)

    px = Horner(listaCoeficienti, x)

    H = calcH(len(listaCoeficienti), px, valDerivataI, valDerivataII)

    if H < 0 : exit(1)

    numitorDeltaX = (valDerivataI + semn * math.sqrt(H))
    if -epsilon <= numitorDeltaX <= epsilon : exit(2)


    deltaX = (len(listaCoeficienti) * valPolinomInX) / numitorDeltaX
    y = x - deltaX

    k = 1
    while abs(deltaX)>= epsilon and k <= kMax and deltaX <= pow(10,8):




if __name__ == '__main__':
    #polinom, listaCoeficienti = citireaPolinomului()
    #print(polinom(1))
    listaCoeficienti = [1, 2, 3, 4, 5]


    R = (abs(listaCoeficienti[0]) + max(listaCoeficienti)) / abs(listaCoeficienti[0])
    print("Radacinele se afla in intervalul: [", -R, ",", R, "]")

    # asta de mai multe ori
    radacina = metodaLuiLaguerre(listaCoeficienti, R, 100)




