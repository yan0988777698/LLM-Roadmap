# Week 03 — NumPy + Matrix Bridge

本週從已完成的 [§2.2 矩陣練習](../math_for_machine_learning/02_linear_algebra/2.2_matrices.py) 接續，練習把多筆資料一起送進 `X @ W + b`。完成條件依 [52 週計畫](../../52_WEEK_PLAN.md)；實際學習結果記在 [PROGRESS.md](../../PROGRESS.md)。

## 今天先做：30–45 分鐘

1. 建立下方環境，開啟 [matrix_bridge.py](matrix_bridge.py)。
2. 先看 `basics` 段落，在紙上預測 `X.shape`、`X[0].shape`、`X[:1].shape`、`X[:, 0].shape`。
3. 執行 `basics`，對照預測。用自己的話說明 `(3,)` 與 `(1, 3)` 的差別。
4. 修改一個索引或切片，再預測一次；記下實際用時與一個疑問。

今天先掌握 shape 與 slicing，後續再接矩陣運算。

## 執行方式（PowerShell）

從 repository 根目錄 `LLM-Engineer-Roadmap` 執行：

```powershell
cd exercises/week03_numpy_matrix_bridge
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe matrix_bridge.py basics
```

若本目錄的 `.venv` 已建立且已安裝 NumPy，只需執行最後一行。後續使用：

```powershell
.\.venv\Scripts\python.exe matrix_bridge.py multiply
.\.venv\Scripts\python.exe matrix_bridge.py broadcast
.\.venv\Scripts\python.exe matrix_bridge.py all
.\.venv\Scripts\python.exe practice.py
```

目前 `practice.py` 已保存完成的五題作答，可直接重跑檢查。最初的練習骨架會提示第一個未完成題目；若要重練，可自行將答案改回 `None`，並保留下方檢查。

`requirements.txt` 固定本次驗證使用的 NumPy 2.5.3。TODO 4 保留手算值為 `expected`，另用 `Y = X @ W + b` 計算，再比較兩者；若更換題目輸入，也要重新手算對應的 `expected`。

## 概念對照

| 概念 | 本週用途 | C# 經驗對照 |
| --- | --- | --- |
| `ndarray` | 儲存同一 dtype 的多維資料 | 可先聯想 `double[,]`，但也支援一維與更高維 |
| `shape` | 每個軸的長度，例如 `(2, 3)` | 二維情況可類比兩個 `GetLength` 的結果 |
| slicing | 選取部分資料 | `X[列範圍, 欄範圍]`，結束索引不包含在內 |
| `reshape` | 保持元素總數，改變形狀 | 重新安排陣列的維度 |
| `*` | 逐元素乘法 | 對應位置相乘 |
| `@` | 矩陣乘法 | 一列與一欄相乘後加總 |
| broadcasting | 對每筆資料套用同一組偏移 | 可聯想在迴圈中重複加上同一組值 |

`X[0]` 會移除被整數索引選取的軸；`X[:1]` 保留該軸。`(3,)` 是一維，不能直接當成二維的列或欄。基本切片會共享原資料；想獨立修改時用 `.copy()`。`reshape` 不等同轉置，例如 `(2, 3)` 改成 `(3, 2)` 並不會自動得到 `X.T` 的內容。[NumPy 官方入門](https://numpy.org/doc/stable/user/absolute_beginners.html)

## 主要實驗：X @ W + b

本週把一列當成一筆資料（sample），一欄當成一個特徵（feature）。一次處理多筆資料稱為 batch。

示範使用：

```python
X = np.array([[1., 2., 3.], [4., 5., 6.]])
W = np.array([[1., 0.], [0., 1.], [1., 1.]])
b = np.array([10., 20.])
```

| 變數 | shape | 意義 |
| --- | --- | --- |
| `X` | `(2, 3)` | 2 筆資料，每筆 3 個特徵 |
| `W` | `(3, 2)` | 將 3 個輸入特徵組合成 2 個輸出 |
| `X @ W` | `(2, 2)` | 每筆資料得到 2 個輸出 |
| `b` | `(2,)` | 2 個輸出各自的偏移值 |
| `X @ W + b` | `(2, 2)` | 每列都加上同一組偏移 |

先手算第一個輸出：`1*1 + 2*0 + 3*1 + 10 = 14`。再自行算剩下三個值，最後執行 `multiply` 核對。

一般二維情況：`(batch, input_features) @ (input_features, output_features)` 得到 `(batch, output_features)`。`*` 不會完成這個加總；示範另用兩個方形矩陣比較兩者，避免只用「有沒有報錯」判斷運算是否正確。

## Broadcasting 除錯

從最右邊的軸開始對齊，每一對長度必須相同，或其中一個是 `1`；缺少的左側軸視為 `1`。否則會出現 `ValueError`。[NumPy broadcasting 規則](https://numpy.org/doc/stable/user/basics.broadcasting.html)

對 `(2, 2)` 的輸出：

- 加 `(2,)`：每個輸出欄位一個偏移。
- 加 `(3,)`：最後一軸的 `2` 與 `3` 不相容。
- 加 `(2, 1)`：可以執行，但變成每列一個偏移；如果目標是每個輸出欄位一個偏移，結果就錯了。

執行 `broadcast` 後，說明報錯案例與「能跑但意思錯了」的差別。不要只靠 reshape 消除錯誤，要先確認每個軸代表什麼。

## 本週安排（預估合計 6h）

| 項目 | 預估 | 工作 |
| --- | ---: | --- |
| 概念 | 1.5h | shape、slicing、reshape、broadcasting；按需對照官方入門 |
| 實作與除錯 | 3.5h | 跟做示範，完成 `practice.py`，修改輸入再驗證 |
| 整理與解釋 | 1h | 記錄手算結果、錯誤原因與獨立解釋 |

與 Week 5 並行時共用每週 6h；以上不是已投入時數。

## 完成標準

- [x] 能解釋 `ndarray` 的 `shape`、`ndim`、`size`、`dtype`。
- [x] 能預測切片的 shape，並在元素總數不變下 reshape。
- [x] 能說明 `*` 與 `@`，並各自算出一個小例子。
- [x] 先手算 `X @ W + b` 的 shape 與數值，再完成 `practice.py` 的檢查。
- [x] 能由 `(4, 3) @ (3, 2) + (2,)` 推出輸出 shape，並說明 batch 改變的影響。
- [x] 找出一個 broadcasting 錯誤，解釋不相容的軸與正確偏移的意義。
- [x] 在進度紀錄填實際用時、驗收結果，區分跟做與獨立完成。

## 學習筆記（自行填寫）

- 實際日期／概念、實作除錯、整理用時：4hrs。
- 我預測的 shape 與實際結果：OK。
- 我遇到的 broadcasting 問題與原因：OK。
- 不看示範也能解釋的部分：OK。
- 尚未理解：無。
