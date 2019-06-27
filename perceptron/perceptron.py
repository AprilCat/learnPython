import numpy as np



def AND(x1, x2):
    w = np.array([0.5, 0.5])
    x = np.array([x1, x2])
    b = -1
    result = np.sum(w * x) + b
    if result >= 0:
        return 1
    else:
        return 0


def OR(x1, x2):
    w = np.array([-0.5, 0.5, 0.5])
    x = np.array([1, x1, x2])
    if np.sum(w * x) >= 0:
        return 1
    else:
        return 0


def NAND(x1, x2):
    w = np.array([-1, 0.5, 0.5])
    x = np.array([1, x1, x2])
    if np.sum(w * x)<0:
        return 1
    else:
        return 0


def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))



if __name__ == "__main__":
    print("AND:")
    print(AND(0, 0))
    print(AND(0, 1))
    print(AND(1, 0))
    print(AND(1, 1))
    print("OR:")
    print(OR(0, 0))
    print(OR(0, 1))
    print(OR(1, 0))
    print(OR(1, 1))
    print("NAND:")
    print(NAND(0, 0))
    print(NAND(0, 1))
    print(NAND(1, 0))
    print(NAND(1, 1))
    print("XOR:")
    print(XOR(0, 0))
    print(XOR(0, 1))
    print(XOR(1, 0))
    print(XOR(1, 1))
