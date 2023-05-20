import numpy as np
import math


def read_b_and_n():
    with open("b5", "r") as file:
        b = []
        n = int(file.readline())
        for line in file:
            b.append(float(line))
    return b, n



def read_sparse_matrix():
    with open("a5", "r") as file:
        n = int(file.readline())
        sparse_matrix = [[] for _ in range(n)]

        for line in file.readlines():
            if len(line.split(',')) > 2:
                line = line.strip('\n').replace(' ', '')
                values = line.split(',')
                value = float(values[0])
                row = int(values[1])
                col = int(values[2])

                if row == col and abs(value) < epsilon:
                    exit(0)

                found_duplicate = False
                for element in sparse_matrix[row]:
                    if element[1] == col:
                        element[0] += value
                        found_duplicate = True

                if not found_duplicate:
                    element = (value, col)
                    sparse_matrix[row].append(element)

    return sparse_matrix



def gauss_seidel(sparse_matrix, x, b, epsilon):
    iteration = 0
    while True:
        sum_squared_diff = 0
        for i in range(len(x)):
            product_sum = 0
            diagonal_value = None

            for element in sparse_matrix[i]:
                if i == element[1]:
                    diagonal_value = element[0]
                else:
                    product_sum += element[0] * x[element[1]]

            if diagonal_value is None:
                print("Elementele de pe diagonala principala sunt nule.")
                exit(0)

            old_x = x[i]
            x[i] = (b[i] - product_sum) / diagonal_value
            sum_squared_diff += (x[i] - old_x) ** 2

        norm = math.sqrt(sum_squared_diff)
        iteration += 1

        if norm < epsilon:
            print("Numarul de iteratii:", iteration)
            return x

        if norm > pow(10, 8):
            print("Divergenta")
            exit(1)




def infinity_norm(A, x, b):
    # Norma = cea mai mare valoare absolută a elementelor
    max_value = 0
    for i in range(len(A)):
        sum_product = 0
        for element in A[i]:
            sum_product += element[0] * x[element[1]]
        diff = abs(sum_product - b[i])
        if diff > max_value:
            max_value = diff
    return max_value



if __name__ == '__main__':
    epsilon = pow(10, -8)
    b, n = read_b_and_n()
    sparse_matrix = read_sparse_matrix()

    x = np.zeros(n)
    x = gauss_seidel(sparse_matrix, x, b, epsilon)
    print(x)

    print("A*x_GS - b = ", infinity_norm(sparse_matrix, x, b))