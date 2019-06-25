def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 1
    if w1*x1 + w2*x2 >= theta:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(AND(0, 0))
    print(AND(0, 1))
    print(AND(1, 0))
    print(AND(1, 1))
