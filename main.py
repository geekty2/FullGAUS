import re
import numpy as np
from bnb import normalize, minus, triangle, last_one
np.set_printoptions(formatter={'float': '{:0.2f}'.format})

while True:
    shape = input("Введіть розмірність матриці, наприклад 6/7 --> 6 rows, 7 columns> ")
    if re.search(r"\d+/\d+", shape):
        break
    else:
        print("Невірно введено розмірність")
        continue

rows, columns = int(shape[0]), int(shape[-1])

x_iter_rows = rows
rows_iter = 1

matrix = []

while x_iter_rows != 0:
    temp = input(f"Введіть дані через пробіл для {rows_iter}-го рядка в к-сті: {columns}> ").split(" ")
    if len(temp) != columns:
        print("Неправильна к-сть значень")
        continue
    else:
        floated_numbers = [float(i) for i in temp]
        matrix.append(floated_numbers)
        x_iter_rows -= 1
        rows_iter += 1
print(matrix)
A = np.array(matrix,dtype=float)

slow = dict()

print(np.round(A, 1))

if __name__ == "__main__":
    for _ in range(A.shape[0]):
        A = normalize(A, slow)
        A = minus(A)
    print(slow)
    print("Трикутна форма", triangle(slow), sep="\n")
    last_one(triangle(slow))
