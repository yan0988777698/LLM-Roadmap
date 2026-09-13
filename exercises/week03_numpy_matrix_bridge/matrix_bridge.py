"""Week 3 guided examples. Predict each shape before running a section."""

import argparse

import numpy as np


def basics() -> None:
    X = np.array([[1., 2., 3.], [4., 5., 6.]])
    print("X:", X, sep="\n")
    print("shape / ndim / size / dtype:", X.shape, X.ndim, X.size, X.dtype)
    for label, value in [("X[0]", X[0]), ("X[:1]", X[:1]),
                         ("X[:, 0]", X[:, 0]), ("X[:, :1]", X[:, :1])]:
        print(label, "shape:", value.shape, "values:", value)
    print("reshape(3, 2):", X.reshape(3, 2), sep="\n")
    print("transpose:", X.T, sep="\n")
    assert not np.array_equal(X.reshape(3, 2), X.T)

    independent = X[:1].copy()
    independent[0, 0] = 99
    assert X[0, 0] == 1
    print("A copied slice can be changed without changing X.")


def multiply() -> None:
    A = np.array([[1., 2.], [3., 4.]])
    B = np.array([[2., 0.], [1., 2.]])
    print("A * B:", A * B, sep="\n")
    print("A @ B:", A @ B, sep="\n")
    np.testing.assert_allclose(A * B, [[2., 0.], [3., 8.]])
    np.testing.assert_allclose(A @ B, [[4., 4.], [10., 8.]])

    X = np.array([[1., 2., 3.], [4., 5., 6.]])
    W = np.array([[1., 0.], [0., 1.], [1., 1.]])
    b = np.array([10., 20.])
    Y = X @ W + b
    print("X / W / b shapes:", X.shape, W.shape, b.shape)
    print("Y shape:", Y.shape)
    print("Y:", Y, sep="\n")
    np.testing.assert_allclose(Y, [[14., 25.], [20., 31.]])


def broadcast() -> None:
    output = np.array([[4., 5.], [10., 11.]])
    bad_bias = np.array([10., 20., 30.])
    try:
        output + bad_bias
    except ValueError as error:
        print("Expected broadcasting error:", error)
    else:
        raise AssertionError("These shapes should be incompatible.")

    feature_bias = np.array([10., 20.])
    row_bias = feature_bias.reshape(2, 1)
    print("Bias per output feature:", output + feature_bias, sep="\n")
    print("Bias per sample (different meaning):", output + row_bias, sep="\n")
    assert not np.array_equal(output + feature_bias, output + row_bias)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("section", choices=["basics", "multiply", "broadcast", "all"],
                        nargs="?", default="basics")
    section = parser.parse_args().section
    for name, demo in [("basics", basics), ("multiply", multiply), ("broadcast", broadcast)]:
        if section in (name, "all"):
            print(f"\n[{name}]")
            demo()


if __name__ == "__main__":
    main()
