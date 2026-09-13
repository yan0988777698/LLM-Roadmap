import numpy as np


def classify(A: np.ndarray, b: np.ndarray) -> str:
    rank_a = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(np.column_stack((A, b)))
    number_of_unknowns = A.shape[1]

    # 當方程組的秩不等於增廣矩陣的秩時，表示無解
    # (rank([A | b]) = rank(A) + 1)
    if rank_a != rank_augmented:
        return "無解"
    # 當方程組的秩等於未知數的個數時，表示唯一解
    if rank_a == number_of_unknowns:
        return "唯一解"
    # 當方程組的秩小於未知數的個數時，表示無限多解
    return "無限多解"


A_no_solution = np.array(
    [
        [1.0, 1.0, 1.0],
        [1.0, -1.0, 2.0],
        [2.0, 0.0, 3.0],
    ]
)

A_unique = np.array(
    [
        [1.0, 1.0, 1.0],
        [1.0, -1.0, 2.0],
        [0.0, 1.0, 1.0],
    ]
)

b_no_solution = np.array([3.0, 2.0, 1.0])
b_unique = np.array([3.0, 2.0, 2.0])
b_infinite = np.array([3.0, 2.0, 5.0])

print(classify(A_no_solution, b_no_solution))  # 無解
print(classify(A_unique, b_unique))  # 唯一解
print(classify(A_no_solution, b_infinite))  # 無限多解

x = np.linalg.solve(A_unique, b_unique)
print(x)  # [1. 1. 1.]
print(np.allclose(A_unique @ x, b_unique))  # True
