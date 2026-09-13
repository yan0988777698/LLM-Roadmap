"""Replace each TODO's None with your answer, then run this file again."""

import numpy as np


def main() -> None:
    X = np.array([[1., 0., 2.], [0., 1., 3.], [2., 1., 0.], [1., 1., 1.]])
    W = np.array([[2., 1.], [1., 0.], [0., 3.]])
    b = np.array([1., -1.])

    # TODO 1：不執行矩陣運算，先填輸出 shape（tuple）。
    predicted_shape = None
    if predicted_shape is None:
        print("TODO 1: Fill predicted_shape before running the calculation.")
        return
    assert predicted_shape == (4, 2), "Revisit batch / input features / output features."

    # TODO 2：取出 X 的第一筆資料，保留二維，shape 應為 (1, 3)。
    first_sample = None
    if first_sample is None:
        print("TODO 2: Fill first_sample with a slice of X.")
        return
    assert first_sample.shape == (1, 3)
    np.testing.assert_array_equal(first_sample, [[1., 0., 2.]])

    # TODO 3：將 b reshape 成二維列，shape 為 (1, 2)。
    bias_row = None
    if bias_row is None:
        print("TODO 3: Reshape b into bias_row.")
        return
    assert bias_row.shape == (1, 2)
    np.testing.assert_array_equal(bias_row, [[1., -1.]])

    # TODO 4：先在紙上手算，再以 NumPy 寫出 XW + b。
    Y = None
    if Y is None:
        print("TODO 4: Compute Y after calculating the values by hand.")
        return
    assert Y.shape == predicted_shape
    np.testing.assert_allclose(Y, [[3., 6.], [2., 8.], [6., 1.], [4., 3.]])

    # TODO 5：bad_bias 不相容。改成每個輸出欄位各加 10、20。
    # 請保留 bad_bias，另填 corrected_bias，並寫下哪一個軸不相容。
    bad_bias = np.array([10., 20., 30.])
    try:
        Y + bad_bias
    except ValueError as error:
        print("Expected error to explain:", error)
    corrected_bias = None
    if corrected_bias is None:
        print("TODO 5: Fill corrected_bias and explain the incompatible axis.")
        return
    np.testing.assert_allclose(Y + corrected_bias,
                               [[13., 26.], [12., 28.], [16., 21.], [14., 23.]])
    print("All practice checks passed. Record your explanations and actual study time.")


if __name__ == "__main__":
    main()
