import numpy as np

A = np.array([[1.0, 2.0, 3.0], [3.0, 2.0, 1.0]])
B = np.array([[0.0, 2.0], [1.0, -1.0], [0.0, 1.0]])

# 矩陣乘法運算
AB = A @ B
BA = B @ A

# 外側決定結果矩陣的形狀，內側決定是否可以相乘
print(AB.shape, AB)
# (2, 3) @ (3, 2) = (2, 2)
print(BA.shape, BA)
# (3, 2) @ (2, 3) = (3, 3)

# 矩陣轉置
assert A.T.shape == (3, 2)

# 兩矩陣相乘的轉置等於兩矩陣轉置後相乘，且順序相反
assert np.allclose((A @ B).T, B.T @ A.T)
# allclose 判斷兩個陣列的所有元素是否在浮點誤差範圍內近似相等

# 單位矩陣運算後不改變原矩陣
identity_left = np.eye(A.shape[0])
identity_right = np.eye(A.shape[1])
assert np.allclose(A @ identity_right, A)
assert np.allclose(identity_left @ A, A)

# 線性方程式求解
M = np.array(
    [
        [2.0, 1.0],
        [5.0, 3.0],
    ]
)
b = np.array([5.0, 13.0])
x = np.linalg.solve(M, b)
assert np.allclose(x, np.array([2.0, 1.0]))
assert np.allclose(M @ x, b)


# Transformers 中的注意力機制
# Query（查詢）：這個 token「想找什麼資訊」
# Key（索引）：這個 token「可以用什麼特徵被找到」
# Value（內容）：被找到後，實際提供的資訊

# X為輸入矩陣，包含4個token，每個token的維度為8
X = np.zeros((4, 8))
# W_q為query權重矩陣，將輸入token的維度8映射到query的維度3
W_q = np.zeros((8, 3))
# W_k為key權重矩陣，將輸入token的維度8映射到key的維度3
W_k = np.zeros((8, 3))
Q = X @ W_q  # (4, 3)
K = X @ W_k  # (4, 3)
# 計算注意力分數矩陣，將query矩陣與key矩陣的轉置相乘
# 內積作為匹配分數，同時受向量方向與長度影響；不是正規化的 cosine similarity。
# 此處只驗證 shape；完整注意力權重還需要縮放與逐列 softmax。
scores = Q @ K.T  # (4, 4)
assert scores.shape == (4, 4)
