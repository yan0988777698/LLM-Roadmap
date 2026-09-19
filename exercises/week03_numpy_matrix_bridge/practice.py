"""Replace each TODO's None with your answer, then run this file again."""

import numpy as np


def main() -> None:
    X = np.array([[1.0, 0.0, 2.0], [0.0, 1.0, 3.0], [2.0, 1.0, 0.0], [1.0, 1.0, 1.0]])
    W = np.array([[2.0, 1.0], [1.0, 0.0], [0.0, 3.0]])
    b = np.array([1.0, -1.0])

    # 本題目標：計算 Y = X @ W + b；@ 表示矩陣乘法，順序是 X 乘 W。
    # TODO 1：先不執行運算，只根據 X、W、b 的 shape，
    # 預測 Y = X @ W + b 的輸出 shape，將答案以 tuple 填入 predicted_shape。
    # 先判斷 X @ W 的 shape，再確認加上 b 時的 broadcasting。
    predicted_shape = (4, 2)
    if predicted_shape is None:
        print(
            "TODO 1: Predict the shape of Y = X @ W + b and fill predicted_shape with a tuple."
        )
        return
    assert predicted_shape == (
        4,
        2,
    ), "Revisit batch / input features / output features."

    # TODO 2：取出 X 的第一筆資料，保留二維，shape 應為 (1, 3)。
    first_sample = X[:1, :]
    if first_sample is None:
        print("TODO 2: Fill first_sample with a slice of X.")
        return
    assert first_sample.shape == (1, 3)
    np.testing.assert_array_equal(first_sample, [[1.0, 0.0, 2.0]])

    # TODO 3：將 b reshape 成二維列，shape 為 (1, 2)。
    bias_row = b.reshape(1, 2)
    if bias_row is None:
        print("TODO 3: Reshape b into bias_row.")
        return
    assert bias_row.shape == (1, 2)
    np.testing.assert_array_equal(bias_row, [[1.0, -1.0]])

    # TODO 4：先在紙上手算 Y = X @ W + b 的數值，再以 NumPy 實作同一個運算。
    expected = np.array([[3.0, 6.0], [2.0, 8.0], [6.0, 1.0], [4.0, 3.0]])
    Y = X @ W + b
    if Y is None:
        print("TODO 4: Compute Y after calculating the values by hand.")
        return
    assert Y.shape == predicted_shape
    np.testing.assert_allclose(Y, expected)

    # TODO 5：bad_bias 不相容。改成每個輸出欄位各加 10、20。
    # 請保留 bad_bias，另填 corrected_bias，並寫下哪一個軸不相容。
    bad_bias = np.array([10.0, 20.0, 30.0])
    try:
        # 最後一個軸（輸出欄位）不相容
        Y + bad_bias
    except ValueError as error:
        print("Expected error to explain:", error)
    else:
        raise AssertionError("The incompatible bias must raise ValueError.")
    corrected_bias = np.array([10.0, 20.0])
    if corrected_bias is None:
        print("TODO 5: Fill corrected_bias and explain the incompatible axis.")
        return
    np.testing.assert_allclose(
        Y + corrected_bias, [[13.0, 26.0], [12.0, 28.0], [16.0, 21.0], [14.0, 23.0]]
    )
    print("All practice checks passed. Record your explanations and actual study time.")


if __name__ == "__main__":
    main()
