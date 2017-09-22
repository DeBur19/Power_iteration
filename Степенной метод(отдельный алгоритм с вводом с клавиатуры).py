import numpy as np
import random

print("Введите размерность матрицы:")
n = int(input())
print("Введите матрицу, элементы разделяйте пробелами, \nстроки - переводами строк:")
A = []
for i in range(n):
    A.append(list(map(float, input().split())))
print("Введите точность:")
eps = float(input())
# создадим случайный вектор соответсвующей размерности:
A = np.array(A)
b = np.random.rand(A.shape[0])
lamb = 0
while True:
    # вычислим образ вектора b:
    b1 = np.dot(A, b)
    # вычислим собственное значение на этой итерации:
    lamb = (b1 @ b) / (b @ b)
    # вычислим норму вектора b1:
    b1_norm = np.linalg.norm(b1)
    # проверим критерий остановки:
    if np.linalg.norm(b1 / b1_norm - b) < eps:
        b = b1 / b1_norm
        break
    # нормируем наш вектор:
    b = b1 / b1_norm
print("Наибольшее собственное значение: ", lamb)
print("Один из соответствующих этому значению собственных векторов: ", b)