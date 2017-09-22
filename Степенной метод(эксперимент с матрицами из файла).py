import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.linalg as sla

inFile = open('Матрицы100.txt', 'r', encoding='utf8')
answers = []
dets = []
n = 0
print("Введите точность:")
eps = float(input())
A = []
for line in inFile:
    line = line.split()
    if len(line) == 1:
        A = []
        n = int(line[0])
    else:
        line = list(map(float, line))
        A.append(line)
        if len(A) == n:
            A = np.array(A)
            dets.append(sla.det(A))
            # создадим случайный вектор соответсвующей размерности:
            b = np.random.rand(A.shape[0])
            lamb = 0
            stopper = True
            while stopper:
                # вычислим образ вектора b:
                b1 = np.dot(A, b)
                # вычислим собственное значение на этой итерации:
                lamb = (b1 @ b) / (b @ b)
                # вычислим норму вектора b1:
                b1_norm = np.linalg.norm(b1)
                # проверим критерий остановки:
                if np.linalg.norm(b1 / b1_norm - b) < eps:
                    stopper = False
                # нормируем наш вектор:
                b = b1 / b1_norm
            answers.append(lamb)
inFile.close()
plt.plot(dets, answers, "bo")
plt.show()