import numpy as np


def normalize(matrix, slow, one_row=[]):
    t = matrix.shape[0]
    x = 0
    for i in matrix[:, 0]:
        for j in matrix[x, :]:
            one_row.append(j / i)
        matrix[x, :] = one_row
        one_row.clear()
        x += 1
    slow[f"x{t}"] = matrix[0, :]
    t -= 1
    return matrix


def minus(matrix, one_row=[]):
    ryad = 1
    while ryad != matrix.shape[0]:
        for i, j in zip(list(matrix[0, :]), list(matrix[ryad, :])):
            one_row.append(j - i)
        matrix[ryad, :] = one_row
        one_row.clear()
        ryad += 1
    matrix = np.delete(matrix, 0, axis=0)
    matrix = np.delete(matrix, 0, axis=1)
    return matrix


def triangle(data):
    max_len = max(len(i) for i in data.values())
    trian = np.zeros((max_len, max_len))
    slow_items = (list(data.items()))

    for i, (k, array) in enumerate(slow_items):
        trian[i, -(len(array)):] = array

    return trian[:-1]


def last_one(mat):
    n = len(mat)
    x = np.zeros(n)

    for i in range(n - 1):
        for j in range(i + 1, n):
            factor = mat[j, i] / mat[i, i]
            mat[j, i:] -= factor * mat[i, i:]
            mat[j, -1] -= factor * mat[i, -1]

    x[n - 1] = mat[n - 1, -1] / mat[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (mat[i, -1] - np.dot(mat[i, i + 1:n], x[i + 1:])) / mat[i, i]

    print("Розв'язок:")
    for i, sol in enumerate(x):
        print(f"x{i + 1} = {sol:.4f}")
    return None
