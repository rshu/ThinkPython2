# Newton Method

def sqrt_root(a, x, epsilon):
    """
    a: find the sqrt root of a
    x: the estimator
    epsilon: a non-distinguishable difference
    """
    while True:
        print(x)
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


if __name__ == "__main__":
    print(sqrt_root(4, 3, 0.0000001))
