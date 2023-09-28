import numpy as np
import random
import math

epsilon = pow(10, -8)


def citireaPolinomului():
    lst = []
    n = int(input("Introduceti numarul de coeficienti : "))
    print("Introduceti coeficientii : ")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    return np.poly1d(lst), lst


def Horner(listaCoeficienti, x):
    bAnterior = listaCoeficienti[0]
    bCurent = 0
    for i in range(1, len(listaCoeficienti)):
        bCurent = listaCoeficienti[i] + bAnterior * x
        bAnterior = bCurent
    return bCurent


def Semn(valoare):
    if valoare < 0:
        return -1
    return 1


def calcH(n, p, pd, pdd):
    return (n - 1) ** 2 * (pd ** 2) - n * (n - 1) * p * pdd


def metodaLuiLaguerre(listaCoeficienti, R, kMax):
    # x0 == x, x1 == y...
    x = random.uniform(-R, R)
    k = 0
    # print(x)
    # ne pregatim de Horner


    polinom = np.poly1d(listaCoeficienti)
    derivataI = polinom.deriv(1)
    coefDerivataI = derivataI.coef

    derivataII = derivataI.deriv(1)
    coefDerivataII = derivataII.coef

    while True:
        #calculam delta
        valPolinomInX = Horner(listaCoeficienti, x)

        valDerivataI = Horner(coefDerivataI, x)
        semn = Semn(valDerivataI)

        valDerivataII = Horner(coefDerivataII, x)

        H = calcH(len(listaCoeficienti)-1, valPolinomInX, valDerivataI, valDerivataII)

        if H < 0:
            print("H < 0")
            exit()

        #print(H)
        numitorDeltaX = (valDerivataI + semn * math.sqrt(H))
        #print(numitorDeltaX, "numitor")
        if -epsilon <= numitorDeltaX <= epsilon:
            print("Numitorul din deltaX este in [-epsilon, epsilon]")
            exit()

        deltaX = (len(listaCoeficienti) * valPolinomInX) / numitorDeltaX

        x = x - deltaX
        k = k + 1

        if abs(deltaX) <= epsilon or k >= kMax or deltaX >= pow(10, 8):
            break
    if epsilon > abs(deltaX):
        return x
    else:
        print("Divergenta!")
        exit()


if __name__ == '__main__':
    # polinom, listaCoeficienti = citireaPolinomului()
    # print(polinom(1))
    listaCoeficienti = [-2,1,2,0,1]

    R = (abs(listaCoeficienti[0]) + max(listaCoeficienti)) / abs(listaCoeficienti[0])
    print("Radacinele se afla in intervalul: [", -R, ",", R, "]")

    listaSolutii = list()

    # asta de mai multe ori
    for i in range(0, 10):
        radacina = metodaLuiLaguerre(listaCoeficienti, R, 100)
        ok = 1
        #print(radacina)
        for j in range(0, len(listaSolutii)):
            if abs(radacina-listaSolutii[j]) < epsilon:
                ok = 0
        if ok == 1:
            listaSolutii.append(radacina)

    print("Solutiile distincte:")
    print(listaSolutii)

    file = open('geek.txt', 'w')
    for i in range(0, len(listaSolutii)):
        file.write(f"{listaSolutii[i]}\n")
    file.close()
